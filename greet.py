def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet('en'), 'Dani')
print(greet('es'), 'Maseya')
print(greet('fr'), 'Dan')
