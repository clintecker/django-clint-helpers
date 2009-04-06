"""
Request Processors I find useful
"""

from django.conf import settings
from django.contrib.sites.models import Site

def site(request):
    """
    Returns context variables required by apps that use Django's Sites app.
    """
    current_site = Site.objects.get_current()
    return {
        'site': current_site,
    }