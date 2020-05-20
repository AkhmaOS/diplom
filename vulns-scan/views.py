import shodan
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import CreateView, ListView, DetailView, TemplateView

from diplom import settings
from .forms import VulnScanForm
from .models import VulnScanModel

api = shodan.Shodan(settings.SHODAN_API_KEY)


class VulnScanView(LoginRequiredMixin, CreateView):
    model = VulnScanModel
    form_class = VulnScanForm
    template_name = 'pentest/vuln_scan.html'
    http_method_names = ['get', 'post', 'options']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.name = form.cleaned_data['name']
        form.instance.site_ip = form.cleaned_data['site_ip']
        shodan_api = api.host(form.cleaned_data['site_ip'])
        form.instance.city = shodan_api['city']
        form.instance.vulns = shodan_api['vulns']
        return super().form_valid(form)


class VulnScanResultView(LoginRequiredMixin, DetailView):
    model = VulnScanModel
    template_name = 'pentest/vuln-scan_result.html'
    http_method_names = ['get', 'options']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        scan_result = VulnScanModel.objects.get(Q(user=self.request.user) & Q(name=self.kwargs['slug']))
        context['api'] = scan_result
        return context

class VulnScanAllView(LoginRequiredMixin, ListView):
    model = VulnScanModel
    template_name = 'pentest/vuln-scan_all.html'
    http_method_names = ['get', 'options']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        scan_result = VulnScanModel.objects.filter(user=self.request.user)
        context['api'] = scan_result
        return context

