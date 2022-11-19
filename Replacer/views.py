from django.shortcuts import render
from django.views.generic import DetailView, ListView, FormView, UpdateView, CreateView, DeleteView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *


class UserLogout(LogoutView):
    next_page = '/login/'


class UserLogin(LoginView):
    authentication_form = UserLoginForm
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = '/'


class TemplateDetailView(LoginRequiredMixin, DetailView):
    model = Template
    template_name = 'Replacer/template_replace.html'
    login_url = '/login/'

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


class HomeView(LoginRequiredMixin, ListView):
    model = Template
    template_name = 'Replacer/template_replace.html'
    login_url = '/login/'


class CreateDocumentView(LoginRequiredMixin, FormView):
    form_class = ReplaceFieldFormUpdate
    template_name = 'Replacer/template_list.html'
    login_url = '/login/'

    def post(self, request, *args, **kwargs):
        self.pk = kwargs.get('pk')
        print(self.pk)
        print(request.POST.getlist('replace_value'))
        return HttpResponse("<h1>Форма принята</h1>")


class TemplateBaseView:
    model = Template
    template_name = 'form.html'
    success_url = reverse_lazy('template_list')
    login_url = '/login/'


class TemplateListView(TemplateBaseView, LoginRequiredMixin, ListView):
    context_object_name = 'template_list'
    template_name = 'Replacer/template_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TemplateBaseForm()
        return context


class TemplateUpdateView(LoginRequiredMixin, TemplateBaseView, UpdateView):
    form_class = TemplateBaseForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Обновить шаблон'
        context['text_button'] = f'Обновить'
        return context


class TemplateCreateView(LoginRequiredMixin, TemplateBaseView, CreateView):
    form_class = TemplateBaseForm


class TemplateDeleteView(LoginRequiredMixin, TemplateBaseView, DeleteView):

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = f'<h3>Вы действительно хотите удалить шаблон</h3><h1>"{context["template"].title}"?</h1>'
        context['text_button'] = f'Удалить'
        return context
