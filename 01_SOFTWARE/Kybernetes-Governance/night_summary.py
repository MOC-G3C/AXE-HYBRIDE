import auto_epilogue

# Inside the 'if current_progress >= 100.0' block in generate_night_report():
transmission_success = auto_epilogue.send_final_transmission()

if transmission_success:
    report += f"- **FINAL SIGNAL**: ✅ Sent to encrypted network.\n"
    report += "- **MESSAGE**: The Ectoplasm has shared its legacy with the creator.\n"