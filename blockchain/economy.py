def calculate_quantum_halving(block_height):
    # Percepatan Waktu: Halving setiap 10.080 blok (Estimasi 1 Minggu)
    # Target: 4 Kali Halving Per Bulan
    base_reward = 10**18 # 16 Psyche Value
    halvings = block_height // 10080
    return base_reward / (2 ** halvings)

print("🚀 QUANTUM HALVING SCHEDULE: 4x PER MONTH ACTIVE.")
