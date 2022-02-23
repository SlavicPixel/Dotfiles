import subprocess

def get_nic_name(interface_type='wireless'):
    try:
        if interface_type == 'wired':
            nic = subprocess.check_output("ifconfig | head -n1 | awk '{print $1;}' | sed 's/://'", shell=True, text=True).strip()
        else:
            nic = subprocess.check_output("ifconfig | grep -o 'wl\w*'", shell=True, text=True).strip()
    except subprocess.CalledProcessError:
        nic = None
    return nic
