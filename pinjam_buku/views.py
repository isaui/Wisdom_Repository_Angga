from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.urls import reverse
from django.contrib import messages
from daftar_buku.models import Buku
from pinjam_buku.models import Peminjaman, Pengembalian
from pinjam_buku.forms import PeminjamanForm
import datetime

# Create your views here.
@login_required(login_url='/login')
def pinjam_buku_outer(request, id):
    buku = Buku.objects.filter(pk=id).first()
    form = PeminjamanForm(request.POST or None, initial={'idBuku': id})
    username = request.user.username
    member = request.user.member
    if member.lower() == "premium":
        hari = 7
    else:
        hari = 3
    hari_kembali = (datetime.datetime.now() + datetime.timedelta(days=hari)).date()
    context = {
        'buku': buku,
        'username': username,
        'member': member,
        'return': hari_kembali,
        'form': form,
    }
    #print(form.is_valid())
    if form.is_valid() and request.method == "POST":
        check = Peminjaman.objects.filter(buku = buku, peminjam=request.user)
        if len(check) != 0:
            messages.warning(request, 'Buku sudah anda pinjam saat ini.')
            return redirect('pinjam_buku:list_pinjam')
        check = Peminjaman.objects.filter(buku = buku)
        if len(check) != 0:
            messages.warning(request, 'Buku sedang dipinjam oleh member lain. Silahkan kembali beberapa saat nanti.')
            return redirect('pinjam_buku:list_pinjam')
        check = Peminjaman.objects.filter(peminjam=request.user)
        if (request.user.member.lower() == "premium"):
            batas = 7
        else:
            batas = 3
        if len(check) >= batas:
            messages.warning(request, 'Batas peminjaman buku sudah tercapai. Silahkan kembalikan beberapa buku yang sudah dipinjam sebelumnya.')
            return redirect('pinjam_buku:list_pinjam')
        peminjaman = form.save(commit=False)
        peminjaman.peminjam = request.user
        peminjaman.buku = buku
        peminjaman.save()
        #print(Peminjaman.objects.all())
        messages.success(request, 'Buku berhasil dipinjam')
        return redirect('pinjam_buku:list_pinjam')
    return render(request, "pinjambuku.html", context)

@login_required(login_url='/login')
def lihatbukudipinjam(request):
    peminjamans = Peminjaman.objects.filter(peminjam = request.user)
    context = {
        'peminjamans': peminjamans
    }
    return render(request, "listbukudipinjam.html", context)

@login_required(login_url='/login')
def get_peminjaman_json(request):
    peminjamans = Peminjaman.objects.filter(peminjam = request.user).values('pk', 'idBuku', 'buku__gambar', 'buku__judul', 'tanggal_dipinjam', 'tanggal_pengembalian')
    peminjaman_list = list(peminjamans)
    return JsonResponse(peminjaman_list, safe=False)

@login_required(login_url='/login')
def get_peminjaman_json_by_id(request, id):
    peminjamans = Peminjaman.objects.filter(pk = id).values('pk', 'idBuku', 'buku__gambar', 'buku__judul', 'peminjam__username', 'peminjam__member', 'tanggal_dipinjam', 'tanggal_pengembalian')
    peminjaman_list = list(peminjamans)
    return JsonResponse(peminjaman_list, safe=False)

@login_required(login_url='/login')
@csrf_exempt
def pengembalian_by_ajax(request):
    if request.method == 'POST':
        id_peminjaman = request.POST.get("idPeminjaman")
        id_buku = request.POST.get("idbuku")
        peminjaman = Peminjaman.objects.filter(pk = id_peminjaman, peminjam=request.user).first()
        peminjaman.delete()
        user = request.user
        buku_dikembalikan = Buku.objects.filter(pk = id_buku).first()
        check_pengembalian = Pengembalian.objects.filter(buku = buku_dikembalikan, peminjam=user)
        if len(check_pengembalian) == 0:
            new_pengembalian = Pengembalian(buku = buku_dikembalikan, peminjam = user, idBuku = id_buku, review = False)
            new_pengembalian.save()
            return HttpResponse(b"CREATED", status=201)
        return HttpResponse(b"DELETED PEMINJAMAN", status=201)
    return HttpResponseNotFound()

@login_required(login_url='/login')
def show_pengembalian(request):
    pengembalians = Pengembalian.objects.filter(peminjam = request.user, review = False)
    context = {
        'pengembalians': pengembalians
    }
    return render(request, "listbukureturn.html", context)