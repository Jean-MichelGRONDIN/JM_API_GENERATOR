def firstLetterToUpperCase(text):
    str = text.copy()
    return str[0].upper() + str[1:]

def firstLetterToLowerCase(text):
    str = text.copy()
    return str[0].lower() + str[1:]

def toTitleCamelCase(text):
    words = text.split('_')
    words = [firstLetterToUpperCase(word) for word in words]
    str = words.join('')
    return str

def toCodeCamelCase(text):
    titleCamelCase = toTitleCamelCase(text)
    return firstLetterToLowerCase(titleCamelCase)

