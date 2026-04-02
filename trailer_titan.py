import time
import sys

def stream_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def start_trailer():
    print("\n" + "="*60)
    stream_text("🚀 [STG-MISSION] : THE VOYAGE OF TITAN-PSYCHE-MONO")
    stream_text("📍 DEPARTURE     : BINTARO COMMAND CENTER, JAKARTA")
    stream_text("🛰️  STATUS        : BREAKING THE ATMOSPHERE...")
    time.sleep(1)
    
    stream_text("🌀 FOLDING SPACE : JAKARTA ↔️ SWISS HUB...")
    stream_text("🌌 WARP DRIVE    : ENGAGED TO GALAXY 700 (16 PSYCHE)")
    time.sleep(1)
    
    print("\n[PROGRESS] : " + "█" * 10 + " 25% (Moon Gravity Assist)")
    time.sleep(0.5)
    print("[PROGRESS] : " + "█" * 25 + " 50% (Mars Slingshot Active)")
    time.sleep(0.5)
    print("[PROGRESS] : " + "█" * 40 + " 100% (DARK MATTER ARRIVAL)")
    
    print("\n🏛️  DESTINATION REACHED. SOVEREIGNTY SECURED.")
    print("💋 MESSAGE: JANGAN AJARI IKAN BERENANG, DRO!")
    print("="*60 + "\n")

if __name__ == "__main__":
    start_trailer()
