import os
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from .models import Servico, Timesheet
from .forms import CriarNovo, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test, login_required
from django.views.decorators.cache import cache_control
from django.conf import settings
from django.db.models import DurationField, ExpressionWrapper, F, IntegerField, Value, Sum
from django.db.models.functions import Coalesce, TruncMonth


@login_required(login_url='/accounts/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def novo(request):
    form = CriarNovo()
    if request.method == 'POST':
        form = CriarNovo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'tracker/novo.html', context)

@login_required(login_url='/accounts/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def timesheet(request):
    c = Timesheet.objects.annotate(
    total_time=ExpressionWrapper(
        ExpressionWrapper(F('saida') - F('entrada'), output_field=IntegerField()) -
        Coalesce(ExpressionWrapper(F('almoco_fim') - F('almoco'), output_field=IntegerField()), Value(0)),
       output_field=DurationField()
    )
)
    
    context = {'c': c}
    return render(request, "tracker/timesheet.html", context)

@login_required(login_url='/accounts/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update(request, id):

	data = Timesheet.objects.get(id=id)
	form = CriarNovo(instance=data)

	if request.method == 'POST':
		form = CriarNovo(request.POST, instance=data)
		
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form, 'data':data}
	return render(request, 'tracker/update.html', context)

@login_required(login_url='/accounts/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete(request, id):
    object = Timesheet.objects.get(id=id)
    object.delete()
    return redirect('/')

###     DASHBOARD

@login_required(login_url='/accounts/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/accounts/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):

    timesheet = Timesheet.objects.values(
    month=TruncMonth('data')
    ).annotate(
        total_time=ExpressionWrapper(
            ExpressionWrapper(F('saida') - F('entrada'), output_field=IntegerField()) - Coalesce(ExpressionWrapper(F('almoco_fim') - F('almoco'), output_field=IntegerField()), Value(0)),
       output_field=DurationField()
    )
    ).order_by('month')

    
    context = {'ct': timesheet}
    return render(request, "tracker/dashboard.html", context)
