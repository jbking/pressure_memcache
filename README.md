# About

An examination returning wrong value from memcache (possibily sharing connection at forking)

# How can you see

```
$ gunicorn -c gunicorn.py pressure_memcache.wsgi
```

then do reload on browser sometime (it will appears in less than 100 secs)
