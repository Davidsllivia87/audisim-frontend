import datetime
import requests
import logging
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

logger = logging.getLogger("logentries")
projectA = {'name':'test_projectA'}
projectB = {'name':'test_projectB'}
projects = [projectA,projectB]
# projects = requests.get("http://localhost:8080/projects/").json()

class NameForm(forms.Form):
    project_name = forms.CharField(label='Nombre de Proyecto')
    project_type = forms.ChoiceField(label='Tipo de proyecto', choices=[('',''),('1','Auditoria'),('2','Otros')])
    project_start_date = forms.DateField(label='Fecha de inicio')
    project_estimated_hours = forms.IntegerField(label='Horas estimadas',min_value=0,max_value=99999)
    project_fees = forms.FloatField(label='Honorarios',min_value=0,max_value=99999)
    project_is_public = forms.BooleanField(label='Entidad de interes publico',required=False)
    project_report_date = forms.DateField(label='Fecha de informe')
    project_letter_date = forms.DateField(label='Fecha de carta')
    project_order_date = forms.DateField(label='Fecha de encargo')

def project_index(request):
    return render(request, 'audisim/project/project_list.html', {'projects':projects})

def project_detail(request):
    return render(request, 'audisim/project/project_detail.html')

def new_project(request):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    success_codes = {requests.codes.ok,
                     requests.codes.no_content,
                     requests.codes.created,
                     requests.codes.accepted
                     }

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():

            response = requests.post("http://localhost:8080/projects/",
                             json={'name': form.cleaned_data['project_name'],
                                   'projectType': 'AUDIT',
                                   'financialStatesDate': [2016, 11, 11],
                                   'estimatedHours': 2,
                                   'startDate': [2016, 11, 1],
                                   'deliveryDate': [2016, 1, 1],
                                   'cost': 2,
                                   'fee': 2,
                                   'orderDate': [2016, 1, 1],
                                   'reportDate': [2016, 1, 1],
                                   'letterDate': [2016, 1, 1],
                                   'publicFees': 1,
                                   }, headers=headers)
            if response.status_code in success_codes:
                return HttpResponseRedirect(reverse('project_index'))
            else:
                return render(request, 'audisim/project/new_project.html', {'new_project_form': NameForm()})
        else:
            return render(request, 'audisim/project/new_project.html', {'new_project_form': NameForm(form.data)})
    else:
        return render(request, 'audisim/project/new_project.html', {'new_project_form': NameForm()})