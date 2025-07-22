def number_of_words(file_contents):
    list_of_words = file_contents.split()
    return len(list_of_words)

def number_of_characters(file_contents):
    chars_dict = {}
    for char in file_contents.lower():
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1

    return chars_dict

def sort_on(items):
    return items["num"]

def sorted_list(chars_dict):
    list = []
    for char in chars_dict:
        list.append({
            "char": char,
            "num": chars_dict[char]
        })
    
    list.sort(reverse=True, key=sort_on)
    return list

