import os
import hashlib

def activate_dark_interference(veto_key):
    print("🌑 INITIALIZING DARK INTERFERENCE PROTOCOL...")
    print("☀️  SOLAR EVENT SHIELD: STANDBY")
    
    # Sensor Siri' na Pacce: Validasi Identitas Arsitek
    # Hanya bisa dibuka dengan Kode Veto "MERDEKA"
    key_hash = hashlib.sha256(veto_key.encode()).hexdigest()
    
    if veto_key == "MERDEKA":
        print("✅ SHIELD ACTIVE: DATA TITAN-PSYCHE TERPROTEKSI DARI RADIASI MATAHARI.")
        print("🌌 INTERFERENSI GELAP: MENGALIRKAN DATA LEWAT MATERI GELAP.")
        return True
    else:
        print("❌ ACCESS REJECTED: ANDA BUKAN ARSITEK! DEKOERENSI DIMULAI...")
        return False

if __name__ == "__main__":
    # Menjalankan Kuitansi 111 dengan Proteksi Gelap
    print("\n--- [BILL] E-KUITANSI QUANTUM (111) ---")
    activate_dark_interference("MERDEKA")
