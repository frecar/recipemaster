from recipemaster import settings


class AnalyticsMiddleware(object):
    def process_template_response(self, request, response):
        if not settings.DEBUG:
            response.context_data['analytics_id'] = getattr(settings, 'ANALYTICS_ID', '')
        return response
