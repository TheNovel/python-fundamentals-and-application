import requests, re, sys


f = input()
linkRE = r"<a [^>]*\s*href=['\"](?!\.\./)(?:\w+://)?([\w\.-]+)(?:.*)['\"]"


res = requests.get(f)
print("\n".join(sorted(list(set(re.findall(linkRE, res.text))))))