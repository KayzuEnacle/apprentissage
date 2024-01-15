import nmap

def scan_network():
    nm = nmap.PortScanner()
    nm.scan(hosts='192.168.1.0/24', arguments='-sn')  # Remplacez l'adresse IP par votre propre plage d'adresses IP

    devices = []
    for host in nm.all_hosts():
        if 'hostname' in nm[host]:
            hostname = nm[host]['hostname']
        else:
            hostname = 'Unknown'
        ip = host
        devices.append({'hostname': hostname, 'ip': ip})

    return devices

def print_devices(devices):
    print("Appareils connectés sur le réseau :")
    print("Nom d'hôte\t\tAdresse IP")
    print("-----------------------------------------")
    for device in devices:
        print(f"{device['hostname']}\t{device['ip']}")
    print("-----------------------------------------")

# Exécuter la fonction de numérisation et afficher les résultats
devices = scan_network()
print_devices(devices)