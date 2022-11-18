from django.shortcuts import render
from django.views.generic import DetailView, ListView, FormView, UpdateView, CreateView, DeleteView, TemplateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *


class TemplateDetailView(DetailView):
    model = Template
    template_name = 'Replacer/template_replace.html'

    def get_form_list(self, fields_list):
        return [ReplaceFieldFormUpdate(instance=field_obj) for field_obj in fields_list]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'], context['path'] = self.pk, self.request.path
        context['form_list'] = self.get_form_list(
            ReplaceField.objects.filter(template_id=self.pk))
        context['field_list'] = ReplaceField.objects.filter(
            template_id=self.pk)
        return context

    def get(self, request, *args, **kwargs):
        self.pk = self.kwargs.get(self.pk_url_kwarg)
        return super().get(request, *args, **kwargs)


class HomeView(ListView):
    model = Template
    template_name = 'Replacer/template_replace.html'


class CreateDocumentView(FormView):
    form_class = ReplaceFieldFormUpdate
    template_name = 'Replacer/template_list.html'

    def post(self, request, *args, **kwargs):
        self.pk = kwargs.get('pk')
        print(self.pk)
        print(request.POST.getlist('replace_value'))
        return HttpResponse("<h1>Форма принята</h1>")


class TemplateBaseView:
    model = Template
    template_name = 'Replacer/template_list.html'
    success_url = reverse_lazy('template_list')


class TemplateListView(TemplateBaseView, ListView):
    context_object_name = 'template_list'


class TemplateUpdateView(TemplateBaseView, UpdateView):
    form_class = TemplateBaseForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Обновить шаблон'
        context['text_button'] = f'Обновить'
        return context


class TemplateCreateView(TemplateBaseView, CreateView):
    form_class = TemplateBaseForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Создать шаблон'
        context['text_button'] = f'Создать'
        return context


class TemplateDeleteView(TemplateBaseView, DeleteView):
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = f'Вы действительно хотите удалить шаблон?'
        context['text_button'] = f'Удалить'
        return context
