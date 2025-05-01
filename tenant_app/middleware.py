from django_multitenant.utils import set_current_tenant
import re

from tenant_app.models import Region


class MultitenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.region_regex = re.compile(r"/api/(?P<region>[^/]+)/")

    def __call__(self, request):
        match = self.region_regex.search(request.path_info)
        region = match.group("region") if match else None
        formatted_region = region.replace("-", " ") if region else None

        if formatted_region:
            region_obj = Region.objects.get(name__iexact=formatted_region)
            if region_obj:
                set_current_tenant(region_obj)
        return self.get_response(request)
