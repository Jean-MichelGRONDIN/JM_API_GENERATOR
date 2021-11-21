def firstLetterToUpperCase(text):
    str = text
    return str[0].upper() + str[1:]

def firstLetterToLowerCase(text):
    str = text
    return str[0].lower() + str[1:]

def toTitleCamelCase(text):
    words = text.split('_')
    words = [firstLetterToUpperCase(word) for word in words]
    str = ''.join(words)
    return str

def toCodeCamelCase(text):
    titleCamelCase = toTitleCamelCase(text)
    return firstLetterToLowerCase(titleCamelCase)

