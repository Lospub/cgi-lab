#!/usr/bin/env python3

import json
import os

# print("Content-type: text/plain")
# print()
# print(os.environ)

# print("Content-type: application/json")
# print()
# print(json.dumps(dict(os.environ), indent=2))

print("Content-type: text/html")
print()
print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")
print(f"<p>QUERY_STRING={os.environ['HTTP_USER_AGENT']}</p>")