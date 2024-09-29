import time
import sys
import random
import shutil

def progress_bar(length, percent):
    bar = '=' * int(length * percent) + ' ' * (length - int(length * percent))
    return f"[{bar}] {int(percent * 100)}%"

def simulate_installation():
    packages = ["lib-insh", "libtorchy", "insh-toolkit", "torchy-utils", "sh-app"]
    for package in packages:
        print(f"Reading package lists... Done")
        print(f"Building dependency tree... Done")
        print(f"Reading state information... Done")
        print(f"The following NEW packages will be installed:")
        print(f"  {package}")
        print(f"0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.")
        print(f"Need to get 1,024 kB of archives.")
        print(f"After this operation, 4,096 kB of additional disk space will be used.")
        print(f"Get:1 http://archive.example.com/ubuntu/ focal/main {package} [1,024 kB]")
        
        for i in range(101):
            sys.stdout.write('\r' + progress_bar(50, i / 100))
            sys.stdout.flush()
            time.sleep(random.uniform(0.01, 0.03))
        print(f"\nSelecting previously unselected package {package}.")
        print(f"(Reading database ... 123456 files and directories currently installed.)")
        print(f"Preparing to unpack .../{package}.deb ...")
        print(f"Unpacking {package} ...")
        print(f"Setting up {package} ...")
        print("Processing triggers for system ...\n")
        time.sleep(random.uniform(0.5, 1.5))
    print("All packages are up to date.\n")
    time.sleep(random.uniform(2, 4))

def simulate_loading_screen():
    tasks = ["Downloading files", "Extracting packages", "Configuring software", "Cleaning up"]
    for task in tasks:
        print(f"{task}...")
        for i in range(20):
            sys.stdout.write('\r[' + '=' * i + '>' + ' ' * (19 - i) + ']')
            sys.stdout.flush()
            time.sleep(random.uniform(0.1, 0.2))
        print(" Done.")
        time.sleep(random.uniform(0.5, 1.5))
    print("Installation complete.\n")
    time.sleep(random.uniform(2, 4))

def simulate_spinner():
    spinner = "|/-\\"
    print("Starting service")
    for _ in range(20):
        for char in spinner:
            sys.stdout.write(f'\r{char} ')
            sys.stdout.flush()
            time.sleep(0.2)
    print("\nService started.\n")
    time.sleep(random.uniform(2, 4))

def simulate_dots():
    print("Connecting to server")
    for _ in range(10):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(random.uniform(0.3, 0.7))
    print(" Connected.")
    print("Syncing data")
    for _ in range(10):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(random.uniform(0.3, 0.7))
    print(" Synced.\n")
    time.sleep(random.uniform(2, 4))

def simulate_percent_complete():
    columns, _ = shutil.get_terminal_size()
    bar_length = columns - 20
    for i in range(101):
        sys.stdout.write(f'\rProcessing: {progress_bar(bar_length, i / 100)}')
        sys.stdout.flush()
        time.sleep(random.uniform(0.05, 0.1))
    print("\nProcessing complete.\n")
    time.sleep(random.uniform(2, 4))

if __name__ == "__main__":
    functions = [
        simulate_installation,
        simulate_loading_screen,
        simulate_spinner,
        simulate_dots,
        simulate_percent_complete
    ]
    while True:
        random.choice(functions)()