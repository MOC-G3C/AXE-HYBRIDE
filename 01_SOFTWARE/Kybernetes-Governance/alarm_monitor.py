import os
import datetime
import haptic_manager

def check_project_slippage(current_predicted_date):
    """Triggers an alert if the completion date slips by more than 7 days."""
    history_path = os.path.expanduser("~/Desktop/L'AXE HYBRIDE/01Software/Kybernetes-Governance/chronos_history.txt")
    
    current_date_obj = datetime.datetime.strptime(current_predicted_date, "%Y-%m-%d")
    
    if os.path.exists(history_path):
        with open(history_path, "r") as f:
            last_date_str = f.read().strip()
            if last_date_str:
                last_date_obj = datetime.datetime.strptime(last_date_str, "%Y-%m-%d")
                
                # Calculate slippage in days
                slippage = (current_date_obj - last_date_obj).days
                
                if slippage > 7:
                    reason = f"DEADLINE SLIPPAGE: +{slippage} days detected."
                    haptic_manager.trigger_haptic_alert(reason)
                    return True, slippage
                    
    # Update history with the new prediction
    with open(history_path, "w") as f:
        f.write(current_predicted_date)
        
    return False, 0