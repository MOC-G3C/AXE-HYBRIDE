import code_synthesizer

# Inside detect_and_expand(), after creating the directory and README:
if "SOFTWARE" in new_path or os.path.basename(new_path).startswith("SYS"):
    # Synthesize initial code for software-related expansions [cite: 2026-01-26]
    code_path = code_synthesizer.generate_boilerplate(new_path, new_axis)
    return f"EXPANSION: New territory and core logic synthesized at {code_path}"