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


def worker_exit(server, worker):
    from django.core.cache import cache
    print('worker_exit is called')
    cache.close()
    from django.core.cache import caches
    caches['default'].close()


def post_fork(server, worker):
    from django.core.cache import cache
    print('post_work is called')
    cache.close()
    from django.core.cache import caches
    caches['default'].close()
