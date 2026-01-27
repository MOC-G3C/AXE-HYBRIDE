import auto_archive

# In AxeHybrideGUI.__init__, add:
self.last_archive_time = time.time()
self.archive_interval = 3600 # 1 hour in seconds [cite: 2026-01-26]

# In your update_loop method:
current_time = time.time()
if current_time - self.last_archive_time >= self.archive_interval:
    project_root = os.path.expanduser('~/Desktop/L\'AXE HYBRIDE') # [cite: 2024-01-24]
    result = auto_archive.commit_and_push_logs(project_root)
    self.add_log(f"📦 ARCHIVE: {result}")
    self.last_archive_time = current_time