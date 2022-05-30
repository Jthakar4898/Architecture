from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
# Create your views here.

# ------------------------------------------Client side----------------------------------------------------------------

#  home page......
def index(request):
	return render(request,'index.html')


#  about page.....
def about(request):
	return render(request,'about.html')



# service page......
def services(request):
	return render(request,'service.html')



# feature page.........
def feature(request):
	return render(request,'feature.html')





#  show portfolio page......
def showportfolio(request):
    data = Portfoliopage.objects.all()
    return render(request, 'portfolio/show_portfolio.html', {'data': data})



#  show detail of portfolio (image gallary).....
def detail_portfolio(request, id):
    context = {}
    context["data"] = Uploadproject.objects.get(id=id)
    return render(request, "portfolio/detail_portfolio.html", context)



#e contact page.....
def contact(request):
    form = ContactsForm()

    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/contact')
    context = {'form': form}
    return render(request, 'contact.html',context)

  







# ------------------------------------------------Admin side-----------------------------------------------------------


# saved message page(conformation page)........................................................................
def saved(request):
    return HttpResponse('successfully uploaded')


# --Dashboard........
@login_required(login_url='login')
def padmin(request):
    data = Contacts.objects.all()
    return render(request, 'padmin.html', {'data': data})



#..Contactlist......
@login_required(login_url='login')
def acontactlist(request):
    data = Contacts.objects.all()
    return render(request, 'acontactlist.html', {'data': data})



# Uploaded portfoliolist....
@login_required(login_url='login')
def aportfoliolist(request):
    data = Portfoliopage.objects.all()
    return render(request, 'aportfoliolist.html', {'data': data})



# uploaded projectlist.....
@login_required(login_url='login')
def aprojectlist(request):
    data = Uploadproject.objects.all()
    return render(request, 'aprojectlist.html', {'data': data})



# upload portfolio(admin side).....
@login_required(login_url='login')
def auploadportfolio(request):
    if request.method == 'POST':
        form = PortfoliopageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/saved')
    else:
        form = PortfoliopageForm()
    return render(request, 'auploadportfolio.html', {'form': form})



# upload project(admin side)-----
@login_required(login_url='login')
def auploadproject(request):
    if request.method == 'POST':
        form = UploadprojectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/saved')
    else:
        form = UploadprojectForm()
    return render(request, 'auploadproject.html', {'form': form})





# ---Update Project detail(admin side).....
@login_required(login_url='login')
def editproject(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Uploadproject, id=id)

    # pass the object as instance in form
    form = UploadprojectForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/aprojectlist")

    # add form dictionary to context
    context["form"] = form

    return render(request, "aeditproject.html", context)



# ------Delete project(admin side)...............
def deleteproject(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Uploadproject, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/aprojectlist")

    return render(request, "aprojectdelete.html", context)



# ...... delete portfolio...................
def deleteportfolio(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Portfoliopage, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/aportfoliolist")

    return render(request, "adeleteportfolio.html", context)


# ----------------------------- Login ,Register, logout---------------------------------------

def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/padmin')

    return render(request, 'register_login.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('/index')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)
                return redirect('/login')

    context = {'form': form, 'page': page}
    return render(request, 'register_login.html', context)

