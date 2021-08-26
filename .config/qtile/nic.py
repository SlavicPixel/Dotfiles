import subprocess

def get_nic_name(): 
    nic = subprocess.check_output("ifconfig | head -n1 | awk '{print $1;}' | sed 's/://'", shell=True, text=True).strip() 
    return nic
