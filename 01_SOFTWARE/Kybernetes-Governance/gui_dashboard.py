import threading
import remote_listener

# In AxeHybrideGUI.__init__:
self.cmd_thread = threading.Thread(
    target=remote_listener.listen_for_remote_commands, 
    args=(self.trigger_exorcism, self.pet.set_mood),
    daemon=True
)
self.cmd_thread.start()