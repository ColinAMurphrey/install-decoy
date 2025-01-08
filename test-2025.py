import time
import random
import sys

def print_loading_bar(length, progress):
    bar = '[' + '#' * progress + ' ' * (length - progress) + ']'
    sys.stdout.write(f'\r{bar}')
    sys.stdout.flush()

def fake_installation():
    loading_phases = [
        "Downloading package",
        "Extracting files",
        "Installing dependencies",
        "Configuring settings",
        "Finalizing installation"
    ]

    for phase in loading_phases:
        print(f"{phase}...")
        total_length = random.randint(20, 50)
        for i in range(total_length + 1):
            print_loading_bar(50, i)
            time.sleep(random.uniform(0.05, 0.2))
        print("\n")

if __name__ == "__main__":
    while True:
        fake_installation()
        print("Installation complete. Restarting...\n")
        time.sleep(2)