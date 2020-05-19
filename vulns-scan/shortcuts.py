import shodan
from django.http import HttpResponse

from .models import VulnScanModel


def get_user_profile(request):
    try:
        profile = VulnScanModel.objects.get(user=request.user)
        return profile
    except VulnScanModel.DoesNotExist:
        HttpResponse('Пожалуйста авторизуйтесь')
