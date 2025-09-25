import os
from collections import defaultdict

FILENAME = "big.txt"  # Replace with your large file path

def count_word_frequencies(filename):
    freqs = defaultdict(int)
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                word = word.lower().strip('.,!?":;()[]{}')  # Normalize words
                if word:
                    freqs[word] += 1
    return freqs

def main():
    if not os.path.exists(FILENAME):
        print("File not found.")
        return

    print(f"Processing {FILENAME}...")
    word_counts = count_word_frequencies(FILENAME)

    # Print the 20 most common words
    sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    print("Top 20 words:")
    for word, count in sorted_counts[:20]:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()