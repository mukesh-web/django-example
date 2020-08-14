from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Mart
from .Forms import MartForm
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User,AnonymousUser




from .utils import render_to_pdf
from django.template.loader import get_template
from django.utils.timezone import datetime


# Create your views here.

def home(request):
    marts=Mart.objects.filter(datecompleted__isnull=True)
    return render(request,'ShipMart/home.html',{'marts':marts})

def index(request):
    user=request.user
    if user.is_authenticated:
        marts=Mart.objects.filter(user=request.user,datecompleted__isnull=True)
        return render(request,'ShipMart/index.html',{'marts':marts})
    else:
        marts = Mart.objects.all()
        messages.error(request, '''Anonymouse User don't have access to this page.<br><b>"Please Sign up and Login first"</b>''')
        return render(request, 'ShipMart/index.html', {'marts': marts})

def create(request):
    user=request.user
    if user.is_authenticated:
        if request.method=="POST":
            form = MartForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                try:
                    martForm=form.save(commit=False)
                    martForm.user=request.user
                    martForm.save()
                    messages.info(request, ' Added 1 Item in list !')
                    return redirect('list')
                except ValueError:
                    messages.warning(request, 'Anonymous User')
                    return render(request, 'ShipMart/create.html', {'forms': form})

            else:
                messages.warning(request,'invalid Form  data')
                return render(request, 'ShipMart/create.html', {'forms': form})

        else:
            form = MartForm()
            return render(request, 'ShipMart/create.html', {'forms': form})
    else:
        messages.error(request,'''Anonymouse User don't have access to this page.<br><b>"Please Sign up and Login first"</b>''')
        return render(request, 'ShipMart/create.html')




def MartList(request):
    user=request.user
    if user.is_authenticated:
        mart = Mart.objects.filter(user=request.user,datecompleted__isnull=True)
        return render(request, 'ShipMart/list.html', {'marts': mart})
    else:
        messages.error(request,'''Anonymouse User don't have access to this page.<br><b>"Please Sign up and Login first"</b>''')
        return render(request, 'ShipMart/list.html')




def MartDetail(request,pk):
    user = request.user
    if user.is_authenticated:
        mart=get_object_or_404(Mart,pk=pk,user=request.user)
        return render(request,'ShipMart/detail.html',{'marts':mart})
    else:
        messages.error(request,'''Anonymouse User don't have access to this page.<br><b>"Please Sign up and Login first"</b>''')
        return render(request, 'ShipMart/detail.html')

def MartUpdate(request,pk):
    user = request.user
    if user.is_authenticated:
        mart = get_object_or_404(Mart, pk=pk,user=request.user)
        form=MartForm(request.POST or None, request.FILES or None,instance=mart)
        if request.method=="POST":
            if form.is_valid():
                form.save()
                messages.info(request, "List 1 item  Updated !")
                return redirect('list')

        else:
            return render(request,'ShipMart/update.html',{'form':form})
    else:
        messages.error(request,'''Anonymouse User don't have access to this page.<br><b>"Please Sign up and Login first"</b>''')
        return render(request, 'ShipMart/update.html')



def MartDelete(request,pk):
    user = request.user
    if user.is_authenticated:
        mart=get_object_or_404(Mart,pk=pk,user=request.user)
        if request.method=="POST":
            mart.delete()
            messages.info(request, "1 item Deleted !")
            return redirect('list')
        else:
            return render(request,'ShipMart/delete.html',{'mart':mart})
    else:
        messages.error(request,'''Anonymouse User don't have access to this page.<br><b>"Please Sign up and Login first"</b>''')
        return render(request,'ShipMart/delete.html')


def MartComp(request):
    user = request.user
    if user.is_authenticated:
        mart=Mart.objects.filter(user=request.user,datecompleted__isnull=False).order_by('-datecompleted')
        return render(request,'ShipMart/complete.html',{'marts':mart})
    else:
        messages.error(request,'''Anonymouse User don't have access to this page.<br><b>"Please Sign up and Login first"</b>''')
        return render(request, 'ShipMart/complete.html')


def MartCopmpleted(request, pk):
    user = request.user
    if user.is_authenticated:
        mart = get_object_or_404(Mart, pk=pk, user=request.user)
        if request.method == 'POST':
            mart.datecompleted = timezone.now()
            mart.save()
            messages.info(request, "List 1 item Completed !")
            return redirect('list')
        else:
            return render(request, 'ShipMart/completed.html', {'tofo': mart})
    else:
        messages.error(request,'''Anonymouse User don't have access to this page.<br><b>"Please Sign up and Login first"</b>''')
        return render(request, 'ShipMart/completed.html')




def generate_pdf(request, pk,):
    user=request.user
    if user.is_authenticated:
        template ='ShipMart/pdf_generator.html'
        marts=get_object_or_404(Mart,pk=pk,user=request.user)
        date=timezone.now()

        pdf = render_to_pdf(template, {'marts':marts,'user':user,'date':date})

        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Grocery_%s.pdf" % marts.title
            content = "inline; filename=%s" % filename
            download = request.GET.get("download")
            if download:
                content = "attachment; filename=%s" % filename
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
    else:
        return HttpResponse("<h2>Anonymouse User don't have access to this page.</h4>"
                            "<h1>'Please Sign up and Login first'</h1>")



























