from __future__ import print_function
preload_app = True
#preload_app = False
workers = 3
max_requests = 5
loglevel = 'warning'


# def pre_fork(server, worker):
#     from django.core.cache import cache
#     print 'pre_fork is called'
#     cache.close()
#     from django.core.cache import caches
#     caches['default'].close()


def close_memcache_connection():
    """
    https://github.com/edx/configuration/pull/2489
    """
    from django.conf import settings
    from django.core import cache as django_cache
    if hasattr(django_cache, 'caches'):
        get_cache = django_cache.caches.__getitem__
    else:
        get_cache = django_cache.get_cache
    for cache_name in settings.CACHES:
        cache = get_cache(cache_name)
        if hasattr(cache, 'close'):
            cache.close()


def worker_exit(server, worker):
    print('worker_exit is called')
    close_memcache_connection()


def post_fork(server, worker):
    print('post_work is called')
    close_memcache_connection()
