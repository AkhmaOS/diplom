from django.views.generic import TemplateView, ListView


class LandingPageView(TemplateView):
    template_name = 'landing/landing.html'
    http_method_names = ['get', 'options']


class BaseView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context
