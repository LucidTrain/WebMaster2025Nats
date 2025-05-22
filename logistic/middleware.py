from django.utils.deprecation import MiddlewareMixin
from ipware import get_client_ip
import geocoder
from .models import Visit
#from .utils import get_client_ip


class VisitMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip, is_routable = get_client_ip(request)
        if ip is None:
            ip = '0.0.0.0'

        # Avoid logging static/media file requests
        if request.path.startswith('/static/') or request.path.startswith('/media/'):
            return

        g = geocoder.ip(ip)
        city = g.city if g.city else ''
        country = g.country if g.country else ''

        Visit.objects.create(
            ip_address=ip,
            city=city,
            country=country
        )
