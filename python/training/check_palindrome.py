'''
Author: Ganesh Manal
Example code: Check if text is palindrome
'''

def is_palindrome(input_text):
    '''
    check if input text is palindrome
    Input: text
    Output: boolean - True if text is palindrome
    '''
    start_index, last_index = 0, len(input_text)-1
    while(start_index <= last_index):
        if input_text[start_index].lower() != input_text[last_index].lower():
            return False
        start_index += 1
        last_index -= 1
    return True


if __name__ == "__main__":
    test_inputs = [
        "madam",
        "racecar",
        "level",
        "mom",
        "rotator",
        "wow",
        "No lemon, no melon"
    ]

    for input_text in test_inputs:
        check_input_text = input_text.replace(" ", "")
        result = is_palindrome(check_input_text)
        print(f"input string: {input_text} --- is palindrome: {result}")
