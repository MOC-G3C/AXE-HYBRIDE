import expansion_engine

# Inside generate_oracle, after the message is chosen:
expansion_log = expansion_engine.detect_and_expand(message)
if expansion_log:
    self.add_log(expansion_log) # [cite: 2026-01-26]