from django.urls import path

from .views import VulnScanView, VulnScanResultView

urlpatterns = [
    path('', VulnScanView.as_view(), name='vulns-scan-scan'),
    path('/result/<slug:slug>', VulnScanResultView.as_view(), name='vulns-scan-result')
]