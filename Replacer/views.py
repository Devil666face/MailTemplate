from django.shortcuts import render
from .models import Template, ReplaceField
from django.views.generic import DetailView, TemplateView, ListView


class ViewTemplate(DetailView):
    model = Template
    template_name = 'Replacer/template_list.html'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['replacefields'] = ReplaceField.objects.filter(template_id=self.pk).select_related('template')
        context['path'] = self.request.path
        return context
 
    def get(self, request, *args, **kwargs):
        self.pk = self.kwargs.get(self.pk_url_kwarg)
        return super().get(request, *args, **kwargs)


class HomeView(ListView):
    model = Template
    template_name = 'Replacer/template_list.html'