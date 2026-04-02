import sys

class STGMonetarySystem:
    def __init__(self):
        # Struktur Nilai Tukar sesuai MONETARY_POLICY.md
        self.symbols = {
            "TPM": "Titan-Psyche-Mono",
            "QS":  "Quorum-State",
            "MET": "Metaportasi",
            "MAC": "Macronesia",
            "QUB": "Qubicoin"
        }
        
        # Base conversion rates (relative to 1 TPM)
        self.rates = {
            "TPM": 1,
            "QS":  1140000,           # 1 TPM = 1.14M QS
            "MET": 11400000000,      # 1 QS = 10K MET
            "MAC": 5700000000000,    # 1 MET = 500 MAC
            "QUB": 5700000000000000  # 1 MAC = 1000 QUB
        }

    def convert(self, amount, from_coin):
        if from_coin not in self.rates:
            print(f"Error: Coin {from_coin} not found in STG Ecosystem.")
            return

        print(f"\n[STG MONETARY ORACLE] Converting {amount:,} {from_coin} ({self.symbols[from_coin]})")
        print("-" * 60)

        # Convert to TPM first as base
        base_val = amount / self.rates[from_coin]

        for coin, rate in self.rates.items():
            result = base_val * rate
            print(f"{coin:<5} : {result:,.2f}")
        
        print("-" * 60)
        print("Status: Rates synchronized with 16 Psyche Equity Alignment.\n")

if __name__ == "__main__":
    stg = STGMonetarySystem()
    
    if len(sys.argv) < 3:
        print("\nUsage: python3 exchange_rate.py [amount] [symbol]")
        print("Example: python3 exchange_rate.py 1 TPM")
        print("Symbols: TPM, QS, MET, MAC, QUB\n")
    else:
        try:
            val = float(sys.argv[1])
            sym = sys.argv[2].upper()
            stg.convert(val, sym)
        except ValueError:
            print("Error: Amount must be a number.")
