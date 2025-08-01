import json
import os
import platform

import requests

# import mathematics


response = requests.get("https://google.com")

print(response.status_code)
print(response.text)
