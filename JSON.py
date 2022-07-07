import ipaddress
import json


def deserialize():
    subnet = input('What is your subnet? ')
    target_subnet = None
    try:
        target_subnet = ipaddress.ip_network(subnet)
    except ValueError:
        print('input not valid')
        return
    database = open("Database.json")
    data = json.load(database)
    site_result = None
    for site in data:
        site_subnet = ipaddress.ip_network(site['ipaddress'])
        if target_subnet.subnet_of(site_subnet):
            site_result = site
            break
    if site_result is None:
        print("Subnet not found")
    else:
        print(site)


deserialize()
