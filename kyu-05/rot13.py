def rot13(message):
    result = ""
    if message:
        for char in message:
            if 65 <= ord(char) <= 90:
                if ord(char) > 77:
                    char = chr(ord(char) + 13 - 90 + 65 - 1)
                else:
                    char = chr(ord(char) + 13)
            elif 97 <= ord(char) <= 122:
                char = chr(ord(char) + 13 - 122 + 97 - 1)
            result += char
    return result
