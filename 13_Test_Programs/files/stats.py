def count_file_stats(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
            
            # Count lines
            f.seek(0)  # move back to start
            lines = f.readlines()
            line_count = len(lines)
            
            # Count words
            words = text.split()
            word_count = len(words)
            
            # Count characters
            char_count = len(text)
            
            return line_count, word_count, char_count
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
        return 0, 0, 0


# Example usage
filename = "tasks.txt"
lines, words, chars = count_file_stats(filename)

print(f"Lines: {lines}")
print(f"Words: {words}")
print(f"Characters: {chars}")
