#! /usr/bin/env python

import argparse
import base64
import io
import urllib.parse
import zlib
from lxml import etree

def main(args):
    p = urllib.parse.urlparse(args.url)
    qs = urllib.parse.parse_qsl(p.query)
    l = [v for k, v in qs if k.lower() == "samlrequest"]
    v = l[0]
    xml = zlib.decompress(base64.b64decode(v), -15).decode('utf-8')
    buf = io.BytesIO(xml.encode('utf-8'))
    doc = etree.parse(buf)
    print(etree.tostring(doc.getroot(), pretty_print=True).decode('utf-8'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decode SAML Requests")
    parser.add_argument(
        "url",
        action='store',
        help="The URL containing the SAML request.")
    args = parser.parse_args()
    main(args)
