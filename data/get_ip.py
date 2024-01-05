import socket
from ip2geotools.databases.noncommercial import DbIpCity
from utils.validation_link import validate_url

url = input("Enter URL: ")
url = validate_url(url)
ip = socket.gethostbyname(url)
response = DbIpCity.get(ip, api_key="free")

print(f"Ip: {ip}")
print(f"City: {response.city}")
print(f"Regio: {response.region}")
print(f"Country: {response.country}")