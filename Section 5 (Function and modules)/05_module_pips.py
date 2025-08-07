import math
import requests

print(math.sqrt(16))
r = requests.get("https://www.google.com")
print(r.text)