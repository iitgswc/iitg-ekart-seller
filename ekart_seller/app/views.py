from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, View

from iitgauth.views import WebmailLoginView

from .forms import ItemForm
from .models import Item


class LoginView(WebmailLoginView):
    template_name = 'app/login.html'
    success_url = reverse_lazy('item-list')


class LogoutView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    http_method_names = ['get', 'options', 'head']

    def get(self, request):
        logout(request)
        return redirect('login')


class ItemCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = ItemForm
    template_name = 'app/item_create.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ItemCreate, self).form_valid(form)


class ItemList(LoginRequiredMixin, ListView):
    template_name = 'app/item_list.html'

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    template_name = 'app/item_detail.html'

    def get_object(self, queryset=None):
        item = Item.objects.get(id=self.kwargs.get('pk'))
        if item.user == self.request.user:
            return item
        else:
            raise Http404()
