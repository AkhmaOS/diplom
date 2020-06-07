from django import forms
from material_widgets.forms import MaterialModelForm

from diplom.forms import FormFieldMixin
from .models import VulnScanModel


class VulnScanForm(FormFieldMixin, forms.ModelForm):
    site_ip = forms.GenericIPAddressField()
    name = forms.CharField(required=True)

    class Meta:
        model = VulnScanModel
        fields = ('name', 'site_ip')