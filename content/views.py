from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group

from .forms import *
from .models import *
from .utils import *


class LinkListView(DataMixin, ListView):
    model = Link
    template_name = 'content/index.html'
    context_object_name = 'link'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Link.objects.all()


class LinkCreateView(PermissionRequiredMixin, DataMixin, CreateView):
    form_class = AddLinkForm
    template_name = 'content/addpage.html'
    permission_required = ('content.add_link', 'content.delete_link', 'content.view_link', 'content.view_category')
    success_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить ссылку")
        return dict(list(context.items()) + list(c_def.items()))


class LinkDeleteView(DataMixin, DeleteView):
    model = Link
    template_name = 'content/detail.html'
    slug_url_kwarg = 'post_slug'
    success_url = reverse_lazy('home')
    context_object_name = 'link'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['link'])
        return dict(list(context.items()) + list(c_def.items()))


class LinkDetailView(DataMixin, DetailView):
    model = Link
    template_name = 'content/detail.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'link'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['link'])
        return dict(list(context.items()) + list(c_def.items()))


class CategoryListView(DataMixin, ListView):
    model = Link
    template_name = 'content/index.html'
    context_object_name = 'link'
    allow_empty = False

    def get_queryset(self):
        return Link.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=str(context['link'][0].cat), cat_selected=context['link'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'content/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Зарегистрироваться")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        user.groups.add(Group.objects.get(name='person'))
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'content/login.html'
    success_url = 'home'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def countofclick(request):
    st = Link.objects.get(slug=request.GET.get('slug'))
    Link.objects.filter(slug=request.GET.get('slug')).update(stat=st.stat+1)
    return HttpResponseRedirect(request.GET.get('next'))
