from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class view1(TemplateView):
    template_name = 'second_task/class_template.html'
    
def view2(request):
    return render(request, 'second_task/function_template.html')
