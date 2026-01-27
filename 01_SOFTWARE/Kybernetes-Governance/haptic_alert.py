import requests
import time

def send_haptic_notification(topic, message):
    """Envoie une notification prioritaire via ntfy.sh."""
    try:
        requests.post(f"https://ntfy.sh/{topic}",
            data=message.encode('utf-8'),
            headers={
                "Title": "⚠️ ALERTE SYSTÈME",
                "Priority": "urgent", # Déclenche la vibration/sonnerie forte
                "Tags": "warning,loudspeaker"
            })
        return True
    except Exception as e:
        print(f"Erreur d'envoi : {e}")
        return False

def monitor_heartbeat(status_callback):
    """Surveille si le signal est toujours actif."""
    topic = "ton_topic_unique_ici" # Remplace par ton sujet ntfy
    
    # Simulation de surveillance
    heartbeat_active = status_callback()
    
    if not heartbeat_active:
        print("Signal perdu ! Envoi du feedback haptique...")
        send_haptic_notification(topic, "Le battement de cœur s'est arrêté. Intervention requise.")