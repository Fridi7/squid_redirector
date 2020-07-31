#!/usr/bin/env python3
import sys
import json
import logging
from logging import handlers
from os.path import getmtime


FILENAME = '/home/fridi/build/data/redirect_list.json'
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address='/dev/log')
log.addHandler(handler)


def getlist():
    try:
        redirect_urls = json.load(open(FILENAME))
        return redirect_urls
    except FileNotFoundError:
        log.error(f'redirector[]: redirect list file not found in directory {FILENAME}')
        sys.exit(1)


def main():
    redirect_urls = getlist()
    time_change = int(getmtime(FILENAME))
    for request in sys.stdin:
        response = ''

        if time_change != int(getmtime(FILENAME)):
            redirect_urls = getlist()
            time_change = int(getmtime(FILENAME))

        url, ip, method = request.split(' ')[:3]

        if method == "CONNECT":
            url = url.replace('www.','')
            url = url.split(':')[0]

        log.debug(f'redirector[]: url: {url} method: {method}')

        if url in redirect_urls.keys():
            response = f'OK rewrite-url="{redirect_urls[url]}"'

        if response:
            log.debug(f'redirector[]: url {url} redirected to {redirect_urls[url]}')

        sys.stdout.write(response + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
