# emoji enhancer: take a sentence, add emoji after keywords

# get a dictionary
emoji_map_fun ={
    "love": "💖",
    "happy": "😊",
    "code": "💻",
}
# get user message
message = input("Enter your message: ")


updated_words = []
# process each word
for word in message.split():
    cleaned = word.lower().strip(".,!?")
    emoji = emoji_map_fun.get(cleaned, "")
    if emoji:
        updated_words.append(f"{emoji}")
    else:
        updated_words.append(word)

updated_message = " ".join(updated_words)
print(updated_message)