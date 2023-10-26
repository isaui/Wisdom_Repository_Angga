from django.shortcuts import render
from .models import Buku
from .forms import ReviewForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect

# def review(request):
#     buku = Buku.objects.last()  # Ambil buku terakhir yang ditambahkan

#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.buku = buku
#             review.save()

#     else:
#         form = ReviewForm()

#     reviews = buku.review_set.all()  # Mengambil semua review yang terkait dengan buku tersebut
#     return render(request, 'reviews.html', {'buku': buku, 'form': form, 'reviews': reviews})

def review(request):
    buku = Buku.objects.last()  # Ambil buku terakhir yang ditambahkan
    form = ReviewForm()
    
    return render(request, 'reviews.html', {'buku': buku, 'form': form})
    
@csrf_exempt
def post_review(request):
    buku = Buku.objects.last()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.buku = buku
            review.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "errors": form.errors})

    return JsonResponse({"message": "Invalid method"})

    # buku = get_object_or_404(Buku, id=book_id)
    # if request.method == 'POST':
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         review = form.save(commit=False)
    #         review.buku = buku
    #         review.save()
    #         return redirect('review', book_id=buku.id)
    # else:
    #     form = ReviewForm()
    # return render(request, 'reviews.html', {'buku': buku, 'form': form})
