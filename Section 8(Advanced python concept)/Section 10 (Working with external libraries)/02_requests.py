import requests

r = requests.get("https://api.github.com/users/codewithharry")

with open("codeWithHarry.txt", "w") as f:
    f.write(r.text)