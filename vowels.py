string = input()

string = string.lower()
vowels = ''

if (string.find('a') != -1):
    vowels = vowels + 'a'
if (string.find('e') != -1):
    vowels = vowels + 'e'
if (string.find('i') != -1):
    vowels = vowels + 'i'
if (string.find('o') != -1):
    vowels = vowels + 'o'
if (string.find('u') != -1):
    vowels = vowels + 'u'
if (vowels == ''):
    vowels = 'none'

print(vowels)