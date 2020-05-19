import shodan
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import CreateView, ListView, DetailView

from diplom import settings
from .forms import PentestScanForm
from .models import VulnScanModel

api = shodan.Shodan(settings.SHODAN_API_KEY)


class VulnScanView(LoginRequiredMixin, CreateView):
    model = VulnScanModel
    form_class = PentestScanForm
    template_name = 'pentest/pentest_scan.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.name = form.cleaned_data['name']
        form.instance.site_ip = form.cleaned_data['site_ip']
        form.instance.scan_type = form.cleaned_data['scan_type']
        shodan_api = api.host(form.cleaned_data['site_ip'])
        form.instance.city = shodan_api['city']
        form.instance.vulns = shodan_api['vulns']
        return super().form_valid(form)


class VulnScanResultView(LoginRequiredMixin, DetailView):
    model = VulnScanModel
    template_name = 'pentest/pentest_result.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        scan_result = VulnScanModel.objects.get(Q(user=self.request.user) & Q(name=self.kwargs['slug']))
        context['api'] = scan_result
        return context
