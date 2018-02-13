import requests, webbrowser

s = requests.get("https://raw.githubusercontent.com/jwfraustro/laughing-waddle/dist/version.txt")

print(s.content)
