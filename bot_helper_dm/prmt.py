from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter

def get_completer():

    completer = NestedCompleter.from_nested_dict({
        'help': None,
        'hello': None,

        'add': {
            'contact': None,
            'phone': None,
            'birthday': None,
            'email': None,
            'address': None,
            'note': None,
            'tegs': None},

        'show': {
            'all': {
                'contacts': None,
                'notes': None}},


        'delete': {
            'contact': None,
            'address': None,
            'note': None},


        'remove': {
            'phone': None,
            'email': None,
            'teg': None},   


        'find': {
            'contact': None,
            'note': None},


        'change': {
            'phone': None,
            'email': None,
            'address': None,
            'note': None},
        
        'days to birthday': None,
        'upcoming birthdays': None,

        'phone': None,
        
        'good bye': None,
        'close': None,
        'exit': None,
        '.': None

    })

    return completer