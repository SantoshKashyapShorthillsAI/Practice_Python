from threading import Thread
import urllib.error
import urllib.request


class HttpRequestThread(Thread):
    def __init__(self, url)->None:
        super().__init__()
        self.url=url
        self.http_status_code=None
        self.reason=None

    def run(self)->None:
        try:
            response =urllib.request.urlopen(self.url)
            self.http_status_code=response.code
        except urllib.error.HTTPError as e:
            self.http_status_code=e.code
        except urllib.error.URLError as e:
            self.reason=e.reason

def main()->None:
    urls=['https://httpstat.us/200', \
        'https://httpstat.us/400']
    
    threads=[HttpRequestThread(url) for url in urls]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    [print(t.http_status_code) for t in threads]

if __name__=='__main__':
    main()