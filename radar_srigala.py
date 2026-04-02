import time
import random

def run_wolf_radar():
    print("\n" + "🛰️  STG RADAR: WOLF DETECTION SYSTEM " + "="*20)
    print("📍 ACTIVE NODES: [BINTARO: 19564] & [CIRACAS: 19546]")
    print("🌌 SCANNING SECTOR: GALAXY 700 (16 PSYCHE)")
    
    # Simulasi Deteksi Intrusi (Srigala)
    threat_level = random.choice(["CLEAR", "CLEAR", "CAUTION", "CLEAR"])
    
    time.sleep(1)
    if threat_level == "CAUTION":
        print("\n🚨 WARNING: SRIGALA/HYENA DETECTED!")
        print("🕵️  ORIGIN: UNAUTHORIZED IP (NATO-ZONE)")
        print("🛡️  ACTION: DEPLOYING SIRI' NA PACCE SHIELD...")
        time.sleep(1)
        print("✅ STATUS: INTRUDER METAPORTATED TO BLACKHOLE.")
    else:
        print("\n✅ STATUS: NO THREATS DETECTED. SECTOR SECURE.")
        print("🔱 MESSAGE: JANGAN AJARI IKAN BERENANG, DRO!")

    print("="*50 + "\n")

if __name__ == "__main__":
    run_wolf_radar()
