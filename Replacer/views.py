from django.shortcuts import render
from django.views.generic import DetailView, ListView, FormView, UpdateView, CreateView, DeleteView
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
        context['under_url'] = reverse_lazy('template_list')
        return context


class TemplateCreateView(LoginRequiredMixin, TemplateBaseView, CreateView):
    form_class = TemplateBaseForm


class TemplateDeleteView(LoginRequiredMixin, TemplateBaseView, DeleteView):

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = f'<h3>Вы действительно хотите удалить шаблон</h3><h1>"{context["template"].title}"?</h1>'
        context['text_button'] = f'Удалить'
        context['under_url'] = reverse_lazy('template_list')
        return context


class FieldsForTemplateView(LoginRequiredMixin, ListView):
    model = ReplaceField
    template_name = 'Replacer/fields_list.html'

    def get(self, request, *args, **kwargs) -> HttpResponse:
        self.pk = kwargs.get('pk')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields_list'] = ReplaceField.objects.filter(
            template=self.pk).select_related('template')
        template = Template.objects.get(pk=self.pk)
        context['form'] = FieldsBaseForm(initial={'template': template, })
        print(context['form']['template'].value())
        return context


class FieldsBaseView(FormView):
    model = ReplaceField
    template_name = 'form.html'
    login_url = '/login/'

    def get_template_pk(self):
        self.pk = self.request.META.get('HTTP_REFERER').split('/')[-2]
        print(f'refer pk = {self.pk}')
        return self.pk

    def get_success_url(self) -> str:
        return reverse_lazy('fields_list', kwargs={'pk': self.template_pk})


class FieldsForTemplateCreateView(LoginRequiredMixin, FieldsBaseView, CreateView):
    form_class = FieldsBaseForm

    def get_success_url(self) -> str:
        return reverse_lazy('fields_list', kwargs={'pk': self.get_template_pk()})


class FieldsForTemplateUpdateView(LoginRequiredMixin, FieldsBaseView, UpdateView):
    form_class = FieldsBaseForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Обновить поле'
        context['text_button'] = f'Обновить'
        context['under_url'] = reverse_lazy(
            'fields_list', kwargs={'pk': self.get_template_pk()})
        return context

    def post(self, request, *args, **kwargs) -> HttpResponse:
        self.template_pk = ReplaceField.objects.get(
            pk=kwargs['pk']).template.pk
        return super().post(request, *args, **kwargs)


class FieldsForTemplateDeleteView(LoginRequiredMixin, FieldsBaseView, DeleteView):

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = f'<h3>Вы действительно хотите удалить поле</h3><h1>"{context["replacefield"].title}"?</h1>'
        context['text_button'] = f'Удалить'
        context['under_url'] = reverse_lazy('fields_list', kwargs={'pk': self.get_template_pk()})
        return context
        
    def post(self, request, *args, **kwargs) -> HttpResponse:
        self.template_pk = ReplaceField.objects.get(
            pk=kwargs['pk']).template.pk
        return super().post(request, *args, **kwargs)