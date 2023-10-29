from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Buku, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/login')  # Tambahkan decorator ini
# def review(request):
#     try:
#         buku = Buku.objects.filter(user=request.user)
#     except Buku.DoesNotExist:
#         # Jika buku untuk pengguna tersebut tidak ditemukan, Anda dapat mengembalikan pesan atau halaman error
#         return redirect('some_other_view_or_url_name')  # Ganti dengan view atau url yang sesuai

#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.buku = buku
#             review.save()
#     else:
#         form = ReviewForm()

#     reviews = buku.review_set.all() if buku else []
#     return render(request, 'reviews.html', {'buku': buku, 'form': form, 'reviews': reviews})

def show_main(request):
    reviews= Reviews.objects.filter(user=request.user)
    context = {
       'review_text': reviews,
    }
    return render(request, "lihat_review.html", context)

@csrf_exempt
@login_required(login_url='/login')  # Perlu login untuk mengakses view ini
def post_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.buku = request.user.buku_set  # Sesuaikan dengan model Anda
            review.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "errors": form.errors})

    return JsonResponse({"message": "Invalid method"})

# @csrf_exempt
# def post_review(request):
#     buku = Buku.objects.filter(user=request.user).last()
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.buku = buku
#             review.save()
#             return JsonResponse({"success": True})
#         else:
#             return JsonResponse({"success": False, "errors": form.errors})

#     return JsonResponse({"message": "Invalid method"})

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

def review(request):
    buku = Buku.objects.last()  # Ambil buku terakhir yang ditambahkan
    form = ReviewForm()
    
    return render(request, 'reviews.html', {'buku': buku, 'form': form})