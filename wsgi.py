from __future__ import print_function
import subprocess
from django.conf import settings

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=('django.contrib.sessions',),
    MIDDLEWARE_CLASSES=('django.contrib.sessions.middleware.SessionMiddleware',),
    ROOT_URLCONF=__name__,
    CACHES={
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': [
                '%(host)s:%(port)d' % {
                    'host': subprocess.check_output('boot2docker ip', shell=True).decode().strip(),
                    'port': 11211,
                }
            ],
        }
    },
    SESSION_ENGINE='django.contrib.sessions.backends.cache',
    SECRET_KEY='the-secret',
)

from django.conf.urls import url  # NOQA
from django.http import HttpResponse  # NOQA


def top(request):
    import random

    if 'v' in request.session and 'v' in request.COOKIES:
        session_value = str(float(request.session['v']))
        cookie_value = str(float(request.COOKIES['v']))
        if session_value == cookie_value:
            s = 'value is available in session and correct'
        else:
            s = 'value is available in session, BUT LEAK\nsession {}, cookie {}'.format(
                session_value,
                cookie_value,
            )
            print('fail', s)
    else:
        s = 'value is not available in session, set a value cookie and session'
    v = random.random()
    response = HttpResponse(s, content_type='text/plain')
    response.set_cookie('v', v)
    request.session['v'] = v
    return response


urlpatterns = (
    url(r'^$', top),
)

if __name__ == 'wsgi':
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
else:
    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
