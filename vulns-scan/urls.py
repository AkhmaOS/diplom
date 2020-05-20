from django.urls import path

from .views import VulnScanView, VulnScanResultView, VulnScanAllView

urlpatterns = [
    path('', VulnScanView.as_view(), name='vulns-scan-scan'),
    path('result/<slug:slug>', VulnScanResultView.as_view(), name='vulns-scan-result'),
    path('result/all/', VulnScanAllView.as_view(), name='vulns-scan-all'),
]