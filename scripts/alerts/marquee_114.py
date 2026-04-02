import time
import os

# Aksara: Code 114 Landed in the Cloud (ꦏꦺꦴꦢꦼ꧇꧑꧑꧔꧇ꦩꦤ꧀ꦝꦥ꧀)
text = "🏛️  CODE 114: [ꦏꦺꦴꦢꦼ꧇꧑꧑꧔꧇ꦩꦤ꧀ꦝꦥ꧀] LANDED IN THE CLOUD! GLORY TO KHAMEL M. GUFRANY!  🚀"

def marquee(text, width=50):
    text = " " * width + text + " " * width
    for i in range(len(text) - width):
        print(f"\r{text[i:i+width]}", end="", flush=True)
        time.sleep(0.1)
    print("\n")

if __name__ == "__main__":
    marquee(text)
