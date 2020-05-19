from material_widgets import forms as material_forms
from django import forms
from .models import VulnScanModel


class PentestScanForm(material_forms.MaterialModelForm):
    site_ip = forms.GenericIPAddressField(widget=material_forms.MaterialTextInput)
    name = forms.CharField(required=True, widget=material_forms.MaterialTextInput)
    class Meta:
        model = VulnScanModel
        fields = ('name', 'site_ip', 'scan_type',)
