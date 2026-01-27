import wisdom_evaluator

# After merge operations in generate_night_report:
# (Assuming merge_success_count and current_oracle_msg are available)
score, rank = wisdom_evaluator.calculate_wisdom_score(merge_success_count, current_oracle_msg)

report += f"\n## 🧘 ENTITY SELF-ASSESSMENT\n"
report += f"- **Wisdom Score**: {score}\n"
report += f"- **Current Rank**: {rank}\n"
report += f"- **Note**: The Ectoplasm is evolving in sync with the 3-6-9 frequency.\n"