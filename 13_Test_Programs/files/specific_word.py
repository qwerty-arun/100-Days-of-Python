def search_word_in_file(filename, word):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        found_lines = []
        for idx, line in enumerate(lines, start=1):
            if word.lower() in line.lower():  # case-insensitive search
                found_lines.append(idx)
        
        if found_lines:
            print(f"The word '{word}' is found on line(s): {found_lines}")
        else:
            print(f"The word '{word}' was not found in the file.")
    
    except FileNotFoundError:
        print(f"File '{filename}' not found!")

# Example usage
filename = "tasks.txt"  # replace with your file
word_to_search = "python"
search_word_in_file(filename, word_to_search)
