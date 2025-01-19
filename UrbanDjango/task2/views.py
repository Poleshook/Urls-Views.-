from django.shortcuts import render
from django.views.generic import TemplateView


def func_template(request):
    return render(request, 'templates/second_task/func_template.html')


class class_template(TemplateView):
    template_name = 'templates/second_task/class_template.html'
