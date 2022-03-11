'''
Author: Ganesh Manal
Example code: Check if text is palindrome
'''

def is_palindrome(input_string):
    '''
    check if input text is palindrome
    Input: text
    Output: boolean - True if text is palindrome
    '''
    start_index, last_index = 0, len(input_string)-1
    while start_index <= last_index:
        if input_string[start_index].lower() != input_string[last_index].lower():
            return False
        start_index += 1
        last_index -= 1
    return True


if __name__ == "__main__":
    text_inputs = [
        "madam",
        "racecar",
        "level",
        "mom",
        "rotator",
        "wow",
        "No lemon, no melon"
    ]

    for text in text_inputs:
        RESULT = is_palindrome(text.replace(" ", ""))
        print(f"\ninput string: {text} \nis palindrome: {RESULT}")
