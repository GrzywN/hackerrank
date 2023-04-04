def swap_case(s: str) -> str:
    letters = []
    
    for letter in s:
        if letter == letter.upper():
            letters.append(letter.lower())
        else:
            letters.append(letter.upper())
                      
    return "".join(letters)
                    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
