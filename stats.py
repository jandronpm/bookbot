def count_words_temp(text):
    words = text.split()
    return len(words)

def count_characters(words):
    characters = {}
    for letter in words:
        if letter.isalpha():
            if letter.lower() in characters:
                characters[letter.lower()] += 1
            else:
                characters[letter.lower()] = 1
    return characters

def sort_character_dict(characters):
    character_list = []

    for key, value in characters.items():
        character_list.append({"letter": key, "count": value})

    character_list.sort(reverse=True, key=lambda character: character["count"])
    return character_list