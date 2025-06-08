# filename: generate_tokens.py
import os
import random
import string
import sys

# Configuration
TOKEN_LENGTH = 6  # Keep it short for legibility, or increase for more noise
CHARSET = string.ascii_lowercase + string.digits
OUTPUT_DIR = '.'

# Accept number of folders as command-line argument
try:
    NUM_TOKENS = int(sys.argv[1])
except (IndexError, ValueError):
    print("Usage: python generate_tokens.py <number_of_folders>")
    sys.exit(1)

def random_token():
    return ''.join(random.choices(CHARSET, k=TOKEN_LENGTH))

def generate_folders(n):
    created = []
    for _ in range(n):
        token = random_token()
        token_path = os.path.join(OUTPUT_DIR, token)
        if not os.path.exists(token_path):
            os.makedirs(token_path)
            readme_path = os.path.join(token_path, 'README.md')
            with open(readme_path, 'w') as f:
                f.write(f"# Token: `{token}`\n\nThis folder may or may not contain signal.\n")
            created.append(token)
    return created

if __name__ == "__main__":
    created_tokens = generate_folders(NUM_TOKENS)
    print("Generated token folders:")
    for token in created_tokens:
        print("  →", token)
