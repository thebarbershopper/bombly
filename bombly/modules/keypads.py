def keypad(extras):
    symbols = str(extras['symbols'])

    groups = [
        ['tennis', 'a', 'l', 'lightning', 'kitty', 'h', 'c'],
        ['e', 'tennis', 'c', 'o', 'star', 'h', 'question'],
        ['copyright', 'but', 'o', 'k', 'r', 'l', 'star'],
        ['six', 'paragraph', 'b', 'kitty', 'k', 'question', 'smile'],
        ['goblet', 'smile', 'b', 'c', 'paragraph', 'three', 'star'],
        ['six', 'e', 'equals', 'smash', 'goblet', 'in', 'omega']
    ]

    print symbols
    curr_symbols = symbols.replace('.', '').lower().split()
    print curr_symbols

    answer = ''
    for group in groups:
        for symbol in curr_symbols:
            if symbol not in group:
                break
        else:
            for symbol in group:
                if symbol in curr_symbols:
                    answer += symbol + ' '

    return answer
