def get_book_text(file_path):
    with open(file_path, "r") as f:
        return f.read()
def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count.keys():
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    sorted_dict = {}
    for i in range(len(dict)):
        max_val = float("-inf")
        
        max_key = None
    
        for key in dict.keys():
            if dict[key] > max_val:
                max_val = dict[key]
                max_key = key
        
        sorted_dict[max_key] = max_val
        del dict[max_key]
    return sorted_dict
         
    

    