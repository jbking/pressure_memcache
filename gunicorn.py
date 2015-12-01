from __future__ import print_function
# set preload_app False take heavy overloading at worker starting.
# it easier to see the failure.
preload_app = True
# preload_app = False
timeout = 300
workers = 16
bind = '127.0.0.1:8000'
max_requests = 5
loglevel = 'warning'


def close_memcache_connection():
    """
    https://github.com/edx/configuration/pull/2489
    """
    from django.conf import settings
    from django.core import cache as django_cache
    if hasattr(django_cache, 'caches'):
        # for 1.8, Django holds some cache objects behind the proxy.
        get_cache = django_cache.caches.__getitem__
        for cache_name in settings.CACHES:
            cache = get_cache(cache_name)
            if hasattr(cache, 'close'):
                cache.close()
    else:
        # for 1.4, Django holds the cache object independently.
        # because that get_cache create new object anytime.
        if hasattr(django_cache.cache, 'close'):
            django_cache.cache.close()


def post_fork(server, worker):
    import wsgi  # NOQA
    #print('post_work is called')
    close_memcache_connection()
