from django.shortcuts import render
from .models import Template, ReplaceField
from .forms import ReplaceFieldForm
from django.views.generic import DetailView, TemplateView, ListView


class ViewTemplate(DetailView):
    model = Template
    template_name = 'Replacer/template_list.html'

    def get_form_list(self, fields_list):
        form_list = [ReplaceFieldForm(instance=field_obj) for field_obj in fields_list]
        print(len(form_list))
        return form_list

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['path'] = self.request.path
        context['form_list'] = self.get_form_list(ReplaceField.objects.filter(template_id=self.pk))
        return context
 
    def get(self, request, *args, **kwargs):
        self.pk = self.kwargs.get(self.pk_url_kwarg)        
        return super().get(request, *args, **kwargs)


class HomeView(ListView):
    model = Template
    template_name = 'Replacer/template_list.html'