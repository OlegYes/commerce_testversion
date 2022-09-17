from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LotForm, ByLotForm, FormComents
from .models import *
from django.views.generic import DetailView


def index(request):
    all_lots = Lots.objects.all()
    return render(request, "auctions/index.html", {"all_lots": all_lots})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


class LotDeteilView(DetailView):
    model = Lots
    template_name = "auctions/lot_view.html"
    context_object_name = "Lot_data"

def testhtml(request):
    all_lots = Lots.objects.all()
    #print(all_lots)
    return render(request, 'auctions/testhtml.html', {"all_lots": all_lots})



def LotData(request, my_lot_id):
    lot = Lots.objects.get(id=my_lot_id)
    #print(f"{lot.close_lot_date.year}-{lot.close_lot_date.month}-{lot.close_lot_date.day }T{lot.close_lot_time.hour }:{lot.close_lot_time.minute }:{lot.close_lot_time.second }Z")
    error = ""
    #lot = Lots.objects.get(id=18)
    if request.method == "POST":
        print(request.POST)
        if request.method == "POST":

            print(request.user, request.POST)
            form = ByLotForm(request.POST)
            # print(form.__dict__)
            if form.is_valid():
                # print(form.cleaned_data['cost_lot'])
                if form.cleaned_data['cost_lot'] >= lot.cost_lot + 10:
                    lot.cost_lot = form.cleaned_data['cost_lot']
                    lot.name_buyer_lot = request.user
                    lot.save()
                else:
                    error = "Your bid must exceed the current bid by at least $10"
            else:
                error = "Error input form"
    else:
        form = LotForm()
    formComent = FormComents()
    # print(formComent)
    #print(form)
    lot_date = lot.close_lot_date
    lot_time = lot.close_lot_time
    t = f"{lot_date}T{lot.close_lot_time}Z"
    return render(request, 'auctions/lot_view.html', {'data': lot, "Time_Close": t, 'form': form, "error": error,
    'none':'', 'formComent': formComent})


def my_lots(request):
    if request.user.is_authenticated:
        my_all_lots = Seller_Lot.objects.filter(name_seller=request.user)
        for i in my_all_lots:
            #print(i)
            my_all_lots_counter = i.lot_id
            #print(my_all_lots_counter)



        data = {"lots": my_all_lots,
                # 'len': my_all_lots_counter
                }



        return render(request, 'auctions/my_lots.html', {'data': my_all_lots})



def addlot(request):
    #print(request.__dict__)
    error =""
    if request.method == "POST":
        form = LotForm(request.POST, request.FILES)
        #print(form.__dict__)


        if form.is_valid():
            #print(form.cleaned_data)


            forma = Lots(
                title=form.cleaned_data['title'],
                text_lot=form.cleaned_data['text_lot'],
                category=form.cleaned_data['category'],
                cost_initial=form.cleaned_data['cost_initial'],
                main_image=form.cleaned_data['main_image'],
                image1=form.cleaned_data['image1'],
                image2=form.cleaned_data['image2'],
                image3=form.cleaned_data['image3'],
                image4=form.cleaned_data['image4'],
                image5=form.cleaned_data['image5'],
                image6=form.cleaned_data['image6'],
                image7=form.cleaned_data['image7'],
                cost_lot=form.cleaned_data['cost_initial'],
                close_lot_date=form.cleaned_data['close_lot_date'],
                close_lot_time=form.cleaned_data['close_lot_time']
            )
            forma.save()
            #print(forma.id)
            seller_lot = Seller_Lot(name_seller=request.user, lot=forma)
            seller_lot.save()
            return redirect("index")
        else:
            error = "Error input form"
    else:
        form = LotForm()
    # Check if authentication successful
    if request.user.is_authenticated:
        data = {'form': form,
                "error": error}
        return render(request, 'auctions/create_lot.html', data)


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
