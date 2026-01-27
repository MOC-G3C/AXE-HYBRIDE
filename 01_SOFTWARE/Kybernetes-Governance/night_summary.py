import neural_bridge

# Inside your generate_night_report function, add:
suggestions = neural_bridge.analyze_semantic_overlap()

# Append to the report string:
report += "\n## 🧠 NEURAL BRIDGE SUGGESTIONS\n"
for s in suggestions:
    report += f"- {s}\n"