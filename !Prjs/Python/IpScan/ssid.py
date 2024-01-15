import subprocess

def get_ssid():
    try:
        command = ['netsh', 'wlan', 'show', 'networks']
        result = subprocess.check_output(command, shell=True, encoding='cp850')
        
        ssid_list = []
        lines = result.split('\n')
        for line in lines:
            if 'SSID' in line:
                ssid = line.split(':')[1].strip()
                ssid_list.append(ssid)

        return ssid_list
    except subprocess.CalledProcessError:
        return []

def scan_networks():
    # Récupérer les SSID de tous les réseaux sans fil disponibles
    ssids = get_ssid()

    # Afficher les SSID
    print('SSID:', ssids)

# Appel de la fonction pour récupérer les SSID des réseaux sans fil
scan_networks()