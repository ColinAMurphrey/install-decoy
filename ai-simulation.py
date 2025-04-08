import time
import os
from random import choice

# Set up colors using ANSI escape codes
class Color:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    CYAN = '\033[35m'
    WHITE = '\033[37m'
    RESET = '\033[0m'

# Function to create a loading spinner animation
def loading_spinner(duration=5):
    chars = ['-', "'", '|', '/']
    end_time = time.time() + duration  # Run for the specified duration
    bar_length = 30  # Length of the loading bar
    while time.time() < end_time:
        for i, char in enumerate(chars):
            elapsed = duration - (end_time - time.time())
            progress = int((elapsed / duration) * bar_length)
            bar = f"[{'#' * progress}{'.' * (bar_length - progress)}]"
            print(f'\r{Color.CYAN}{char} {bar} Processing...', end='')
            time.sleep(0.1)
            os.system('cls' if os.name == 'nt' else 'clear')

# Function to create a matrix-like falling text effect
def matrix_effect(duration=5):
    chars = '0123456789abcdef'
    end_time = time.time() + duration  # Run for the specified duration
    while time.time() < end_time:
        for y in range(8, 0, -1):
            x = choice(chars)
            print(f'\r{Color.GREEN}{x}', end='')
            time.sleep(0.05)
            os.system('cls' if os.name == 'nt' else 'clear')

# Function to simulate AI processing text
def ai_processing(duration=5):
    messages = [
        "Analyzing data patterns...",
        "Identifying key features...",
        "Calculating probabilities...",
        "Optimizing neural network weights...",
        "Generating response..."
    ]
    bar_length = 30  # Length of the progress bar
    end_time = time.time() + duration  # Run for the specified duration
    while time.time() < end_time:
        for msg in messages:
            elapsed = duration - (end_time - time.time())
            progress = int((elapsed / duration) * bar_length)
            bar = f"[{'#' * progress}{'.' * (bar_length - progress)}]"
            print(f'\r{Color.WHITE}{msg} {bar}', end='')
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    while True:  # Infinite loop to run the simulation continuously
        # Clear the screen and display the starting message
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""
{Color.BLUE}╭╮═══════════════════════════════════╮╭════════╗
││                                          ││        │
││ {Color.CYAN}[AI SIMULATION STARTING] {Color.RESET}   ││        │
││                                          ││        │
╰╯═══════════════════════════════════╯╰════════╝{Color.RESET}
        """)

        # Run the functions sequentially with limited durations
        loading_spinner(duration=5)
        matrix_effect(duration=5)
        ai_processing(duration=5)

        # Optional: Add a short pause before restarting the loop
        time.sleep(2)