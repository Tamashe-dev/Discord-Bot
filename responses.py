from random import choice, randint





def get_response(user_input: str) -> str:
        lowered: str = user_input.lower()

        if lowered == '':
                return 'Leeech mabte7kiniich brooo'
        elif 'salam','bonjour','wsh','bjr','slm','hello' in lowered:
                return 'Salaam brooooo!'
        else:
                return choice(['Broo je n\'ai pas compris...',
                               'De quoi tu paaarle?',
                               'Repeeete ya charmoota'])
                                
