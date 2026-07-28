from django.conf import settings
from accounts.decorators import is_owner


def app_branding(request):
    return {
        "APP_NAME": settings.APP_NAME,
        "APP_TAGLINE": settings.APP_TAGLINE,
        "is_owner": is_owner(request.user),
    }
