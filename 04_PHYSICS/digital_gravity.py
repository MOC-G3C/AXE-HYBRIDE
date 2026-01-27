def calculate_gravity(bpm, load):
    """
    Calculates digital gravity pull.
    High CPU load increases 'mass', stabilizing the system's pulse.
    """
    # Tesla-inspired constant
    G_CONSTANT = 6.674 
    system_mass = (load * 10) + 1
    
    # Gravitational pull calculation
    pull = (G_CONSTANT * system_mass) / max((bpm / 60), 1)
    return round(pull, 4)