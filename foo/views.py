from __future__ import print_function
import random
from django.http import HttpResponse


def index(request):
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
