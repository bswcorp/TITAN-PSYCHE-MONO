import random

def nasa_validation_protocol():
    print("🛰️  TITAN-PSYCHE MISSION: INITIALIZING SENSORS...")
    
    # 1. GRNS: Deteksi Gamma-Ray (Besi & Nikel Digital)
    grns_scan = random.uniform(0.8, 1.0) 
    # 2. Imager: Silikat vs Logam Murni
    imager_ratio = random.uniform(0.7, 0.9)
    # 3. Magnetometer: Jejak Magnetik Inti Planet
    mag_field = random.choice([True, True, False])

    if grns_scan > 0.85 and imager_ratio > 0.75 and mag_field:
        print("💎 MATERIAL DETECTED: HIGH DENSITY NICKEL-IRON CORE.")
        return True
    else:
        print("🪨 WARNING: SILICATE ROCK DETECTED. MINING REJECTED.")
        return False

def halving_gravity_check(block_height):
    # Gravity Science: Semakin tinggi blok, semakin berat "tarikan" (Difficulty)
    base_reward = 10**18 # Nilai 16 Psyche
    halvings = block_height // 210000
    current_reward = base_reward / (2 ** halvings)
    print(f"⚖️  GRAVITY SCIENCE: BLOCK {block_height} | REWARD: {current_reward} TPQ")
    return current_reward
