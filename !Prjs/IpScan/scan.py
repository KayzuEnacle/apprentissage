import netifaces
import ipcalc
import subprocess

def get_ssid(interface):
    try:
        command = ['netsh', 'wlan', 'show', 'networks', 'mode=Bssid']
        result = subprocess.check_output(command, shell=True)
        result = result.decode('cp850')
        
        ssid_list = []
        lines = result.split('\r\n')
        for line in lines:
            if 'SSID' in line:
                ssid = line.split(':')[1].strip()
                ssid_list.append(ssid)

        return ssid_list
    except subprocess.CalledProcessError:
        return []

def scan_networks():
    # Récupérer toutes les interfaces réseau disponibles
    interfaces = netifaces.interfaces()

    for interface in interfaces:
        # Récupérer les adresses IP de l'interface réseau
        addresses = netifaces.ifaddresses(interface)
        
        if netifaces.AF_INET in addresses:
            addresses = addresses[netifaces.AF_INET]
            
            for address in addresses:
                ip = address['addr']
                netmask = address['netmask']
                
                # Calculer le réseau en fonction de l'adresse IP et du masque
                network = ipcalc.Network(ip, netmask)
                
                # Récupérer les SSID des autres réseaux sans fil disponibles
                ssids = get_ssid(interface)
                
                # Afficher les SSID, l'adresse IP et le réseau correspondant
                for ssid in ssids:
                    print('SSID:', ssid)
                    print('Adresse IP:', ip)
                    print('Réseau:', str(network.network()))
                    print('-' * 40)

# Appel de la fonction pour scanner les réseaux
scan_networks()