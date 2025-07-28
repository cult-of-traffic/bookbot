def count_of_words(text):
    return len(text.split())

def count_of_symbols(text):
    result = {}

    for ch in text.lower():
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1

    return result

def sort_of_symbols_stat(dict):
    arr = []
    for key, value in dict.items():
        arr.append({"char": key, "num": value })

    arr.sort(reverse = True, key = lambda i: i["num"])

    return arr
