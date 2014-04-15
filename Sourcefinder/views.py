from django.views.generic import RedirectView
from django.core.urlresolvers import reverse

class IndexView(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self):
        return '/findSource'
