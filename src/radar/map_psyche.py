import time
import random

def draw_star_map():
    stars = ["*", ".", ".", "o", "°", " "]
    print("\n" + "🌌 STG STAR MAP: SECTOR GALAXY 700 " + "="*20)
    
    # Generate Starfield
    for _ in range(10):
        line = "".join(random.choice(stars) for _ in range(50))
        if _ == 5:
            # The Position of 16 Psyche
            print(line[:20] + "  ☄️ [16 PSYCHE]  " + line[35:])
        else:
            print(line)
            
    print("="*50)
    print("📍 COORDINATES : 2.92 AU FROM SUN")
    print("💎 COMPOSITION : 85% IRON-NICKEL CORE")
    print("🛡️  STATUS      : SOVEREIGN MINING ACTIVE")
    print("="*50 + "\n")

if __name__ == "__main__":
    draw_star_map()
