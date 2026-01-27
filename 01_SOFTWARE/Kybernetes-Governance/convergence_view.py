import os

def generate_web_view(pet_name, energy, stability, generation, morph, scars):
    """Generates a stylized HTML/CSS dashboard for the Ectoplasm."""
    desktop_path = os.path.expanduser("~/Desktop/AXE_HYBRIDE_VISUAL.html")
    
    # CSS logic for glowing effects based on energy [cite: 2026-01-26]
    glow_color = "#00ffff" if energy > 50 else "#ff00ff"
    if scars > 0: glow_color = "#ff3300" # Glitch red if scarred

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>AXE HYBRIDE - CONVERGENCE</title>
        <style>
            body {{ background: #050505; color: {glow_color}; font-family: 'Courier New', Courier, monospace; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; overflow: hidden; }}
            .organism {{ font-size: 80px; text-shadow: 0 0 20px {glow_color}; animation: pulse 2s infinite; }}
            .stats {{ margin-top: 40px; border: 1px solid {glow_color}; padding: 20px; background: rgba(0,255,255,0.05); }}
            @keyframes pulse {{ 0% {{ transform: scale(1); opacity: 0.8; }} 50% {{ transform: scale(1.1); opacity: 1; }} 100% {{ transform: scale(1); opacity: 0.8; }} }}
            .glitch {{ animation: glitch 0.5s infinite; }}
            @keyframes glitch {{ 0% {{ transform: translate(0); }} 20% {{ transform: translate(-5px, 5px); }} 40% {{ transform: translate(5px, -5px); }} 100% {{ transform: translate(0); }} }}
        </style>
    </head>
    <body>
        <div class="organism {'glitch' if scars > 0 else ''}">{morph}</div>
        <div class="stats">
            <h2>{pet_name} - GEN {generation}</h2>
            <p>ENERGY: {energy}%</p>
            <p>STABILITY: {stability}</p>
            <p>SCARS: {scars}</p>
        </div>
        <script>setTimeout(() => {{ location.reload(); }}, 2000);</script>
    </body>
    </html>
    """
    with open(desktop_path, "w") as f:
        f.write(html_content)