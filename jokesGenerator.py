# https://github.com/pyjokes/pyjokes
import pyjokes

def generate():
    # choose language of the joke
    languages = {'english': 'en', 'german': 'de', 'spanish': 'es', 'italian': 'it', 'galician': 'gl', 'basque': 'eu'}
    language_input = input('In which language do you want the joke?: ')
    for key in languages:
        if language_input.lower() == key:
            language_choosen = languages[key]
            break

    # create message with the joke
    message_text = pyjokes.get_joke(language=language_choosen, category='neutral')

    return message_text
