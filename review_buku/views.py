from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Buku, Review
from .forms import ReviewForm


from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')  # Tambahkan decorator ini jika Anda memerlukannya
def review(request, id):
    buku = Buku.objects.filter(pk=id).first()
    form = ReviewForm(request.POST or None, initial={'idBuku': id})
    username = request.user.username
    member = request.user.member
    context = {
        'buku': buku,
        'username': username,
        'member': member,
        'form': form,
    }
    return render(request, "review.html", context)

def show_reviews(request, id):
    reviews = Review.objects.filter(buku_id=id)  # Mengambil semua ulasan untuk buku dengan ID yang sesuai
    return render(request, 'lihat_review.html', {'reviews': reviews})

@csrf_exempt
@login_required(login_url='/login')  # Perlu login untuk mengakses view ini
def post_review(request):
    if request.method == "POST":
        
        text = request.POST.get('review_text')
        print(request.POST.get('idBuku'))
        print(request.POST.get('review_text'))
        buku = Buku.objects.get(pk= int(request.POST.get('idBuku')))
        review = Review(review_text=text, buku=buku)
        review.save()
        return JsonResponse({"success": True})
    

    return JsonResponse({"message": "Invalid method"})