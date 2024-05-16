
def get_responses(user_input: str ) -> str: 
    lowered: str = user_input.lower()
    if lowered== '':
        return 'Can you repeat that?'
    elif 'hello' in lowered:
        return 'hello!'
    elif 'dice roll' in lowered:
        return f'you rolled: {randint(1,6)}'
    elif 'spring' in lowered:
        return 'boing - - ribbit '
    else:
        if 'sleep' in lowered:
            return 'Goodnight'
        else:
            return choice(['I don/'t know what to say',
                            'Put together a comprehensible sentence please',
                            'You smell funny'])
