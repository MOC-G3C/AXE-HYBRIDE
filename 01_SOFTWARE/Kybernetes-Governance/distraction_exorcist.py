import os

def cast_exorcism():
    """Blocks distracting websites by modifying the hosts file. 
    Requires script to be run with sudo or appropriate permissions.
    """
    hosts_path = "/etc/hosts"
    redirect = "127.0.0.1"
    distractions = [
        "www.youtube.com", "youtube.com",
        "www.reddit.com", "reddit.com",
        "www.facebook.com", "facebook.com",
        "www.twitter.com", "twitter.com"
    ]
    
    print("⚔️ EXORCISM: Purging distractions from the simulation...")
    
    try:
        with open(hosts_path, "a") as hosts:
            for site in distractions:
                hosts.write(f"\n{redirect} {site}")
        return True
    except PermissionError:
        print("❌ ERROR: Exorcism requires administrative rituals (sudo).")
        return False

def lift_curse():
    """Restores the hosts file by removing the redirection entries."""
    hosts_path = "/etc/hosts"
    
    try:
        with open(hosts_path, "r") as f:
            lines = f.readlines()
            
        with open(hosts_path, "w") as f:
            for line in lines:
                if "127.0.0.1" not in line or not any(site in line for site in ["youtube", "reddit", "facebook", "twitter"]):
                    f.write(line)
        print("✨ CURSE LIFTED: Focus restored. Access granted.")
        return True
    except PermissionError:
        return False