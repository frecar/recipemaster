from django.conf import settings


def analytics(request):
    if not settings.DEBUG:
        return {'analytics_id': getattr(settings, 'ANALYTICS_ID', '')}
    return {}
