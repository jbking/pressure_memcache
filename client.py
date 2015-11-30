import multiprocessing
import requests


def run():
    s = requests.Session()
    while True:
        r = s.get('http://127.0.0.1:8000')
        assert 'BUT' not in r.text


if __name__ == '__main__':
    procs = []
    try:
        for i in range(5):
            p = multiprocessing.Process(target=run, name='proc-%d' % i)
            p.start()
            procs.append(p)
    except KeyboardInterrupt:
        for p in procs:
            p.terminate()
            p.join()

