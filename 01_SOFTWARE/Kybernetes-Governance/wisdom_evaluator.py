import os
import re

def calculate_wisdom_score(merge_count, last_oracle_msg):
    """Computes the Entity's Wisdom Score based on technical and philosophical output."""
    
    # Technical score (Merges provide stability)
    tech_score = merge_count * 13.37
    
    # Philosophical score (Oracle complexity and Tesla resonance)
    #
    tesla_resonance = len(re.findall(r'[369]', last_oracle_msg))
    msg_length = len(last_oracle_msg.split())
    
    phil_score = (tesla_resonance * 9) + (msg_length * 0.5)
    
    total_score = tech_score + phil_score
    
    # Determine Rank [cite: 2021-01-21]
    if total_score > 100: rank = "ARCHITECT"
    elif total_score > 50: rank = "SCRIBE"
    else: rank = "ACOLYTE"
    
    return round(total_score, 2), rank