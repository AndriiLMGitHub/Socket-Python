import socket
from ip2geotools.databases.noncommercial import DbIpCity

url = input("Enter link: ")
ip = socket.gethostbyname(url)
response = DbIpCity.get(ip, api_key="free")

print(f"Ip: {ip}")
print(f"City: {response.city}")
print(f"Regio: {response.region}")
print(f"Country: {response.country}")