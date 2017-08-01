#!/usr/bin/env python3

#HALP Test the DataUploadServlet.

import requests, io, zipfile

def createzip(filedata):
    zipdata = io.BytesIO()
    with zipfile.ZipFile(zipdata, 'w') as zf:
        zf.writestr(zipfile.ZipInfo('woo.txt'), filedata) # Use ZipInfo constructor for deterministic update time.
    zipdata.seek(0)
    return zipdata

def main():
    port = int(input('Port? '))
    text = input('Text? ')
    r = requests.post("http://localhost:%s/upload/attachment" % port, files = {
        'ignored1': createzip(text + '1'),
        'ignored2': createzip(text + '2'),
    })
    print(r.text)

if '__main__' == __name__:
    main()
