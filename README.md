# About This

An examination to check session **leak** (memcache backed cache based session leak) with Django.
This means a session loads wrong data from memcache by `SESSION_KEY` which in correspond cookie.
It might be bug sharing connection at forking on gunicorn.

Tested with Django 1.4.21 and 1.8.7, others see `requirements.txt`

# How to reproduce

1. run gunicorn

   ```
   $ gunicorn -c gunicorn.py wsgi
   ```

2. pressure the instance with the client

   ```
   $ python client.py
   ```

3. open the url with a browser, then repeat reloading.
4. you sometime see a fail on gunicorn's output or browser.
