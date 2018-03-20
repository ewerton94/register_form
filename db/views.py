# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import CandidateForm
from .models import Candidate
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.semester = int(form.semester)
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Inscrição realizada com sucesso!')
            return render(request, 'index.html', {})
            
    return render(request, 'index.html', {'form': CandidateForm})
