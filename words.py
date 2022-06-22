def print_upper_words(words, starting_letters):
    for word in words:
        for start in starting_letters:
            if word.startswith(start) or word.startswith(start.upper()):
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "eebydeeby"], ["h", "g"])