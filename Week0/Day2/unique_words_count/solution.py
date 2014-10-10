def unique_words_count(arr):
    help_arr = []
    unique_words_couter = 0
    for word in arr:
        if word not in help_arr:
            unique_words_couter += 1
            help_arr.append(word)
    return unique_words_couter

