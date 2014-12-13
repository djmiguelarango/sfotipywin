from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, HttpResponse
from django.views.generic import View, TemplateView, RedirectView, FormView
from userprofiles.forms import UserCreationEmailForm, EmailAuthenticationForm, LoginForm
from userprofiles.mixins import LoginRequiredMixin


def signup(req):
    form = UserCreationEmailForm(req.POST or None)

    if form.is_valid():
        form.save()

    return render(req, 'signup.html', {'form': form})


def signin(req):
    form = EmailAuthenticationForm(req.POST or None)

    if form.is_valid():
        login(req, form.get_user())

    return render(req, 'signin.html', {'form': form})


# class LoginView(View):

#     def get(self, request, *args, **kwargs):
#         return HttpResponse('LoginView !!!')

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/profile/'

    def form_valid(self, form):
        # username = form.cleaned_data['username']
        # password = form.cleaned_data['password']

        # user = authenticate(username=username, password=password)

        # if user is not None:
        #     if user.is_active:
        #         login(self.request, user)
        # else:
        #     self.success_url = '/login/'

        login(self.request, form.get_user())

        return super(LoginView, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        is_auth = False
        name = None

        if self.request.user.is_authenticated():
            is_auth = True
            name = self.request.user.username

        data = {
            'is_auth': is_auth,
            'name': name
        }

        context.update(data)

        return context

# class LoginView(TemplateView):
#     template_name = 'login.html'

#     def get_context_data(self, **kwargs):
#         context = super(LoginView, self).get_context_data(**kwargs)
#         is_auth = False
#         name = None

#         if self.request.user.is_authenticated():
#             is_auth = True
#             name = self.request.user.username

#         data = {
#             'is_auth': is_auth,
#             'name': name
#         }

#         context.update(data)

#         return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated():
            context.update({'userprofile': self.get_userprofile})

        return context

    def get_userprofile(self):
        return self.request.user.userprofile


class PerfilRedirectView(RedirectView):
    # url = '/profile/'
    pattern_name = 'profile'
