from allauth.account.views import LoginView, SignupView


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'


class AccountSingUpView(SignupView):
    template_name = 'accounts/signup.html'
