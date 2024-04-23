import enchant

def is_english_word(word):
    d = enchant.Dict("en_US")  # Using the US English dictionary
    return d.check(word)

def is_mostly_english(text, threshold):
    words = text.split()
    english_word_count = sum(1 for word in words if is_english_word(word))
    english_word_ratio = english_word_count / len(words)
    return english_word_ratio >= threshold