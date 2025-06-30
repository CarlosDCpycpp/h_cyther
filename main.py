from typing import Callable

# char -> h
reverse_crypt: dict[str, str] = {
    'a': 'h',
    'b': 'H',
    'c': 'Hh',
    'd': 'HH',
    'e': 'Hhh',
    'f': 'HhH',
    'g': 'HHh',
    'h': 'HHH',
    'i': 'Hhhh',
    'j': 'HhhH',
    'k': 'HhHh',
    'l': 'HhHH',
    'm': 'HHhh',
    'n': 'HHhH',
    'o': 'HHHh',
    'p': 'HHHH',
    'q': 'Hhhhh',
    'r': 'HhhhH',
    's': 'HhhHh',
    't': 'HhhHH',
    'u': 'HhHhh',
    'v': 'HhHhH',
    'w': 'HhHHh',
    'x': 'HhHHH',
    'y': 'HHhhh',
    'z': 'HHhhH',
    '&': 'HHhHh'
}

# h -> char
crypt: dict[str, str] = {v: k for k, v in reverse_crypt.items()}


def cryptor(table: dict[str, str], input_sep: str | bool, output_sep: str = '') -> Callable:

    def wrapper(func: Callable) -> Callable:  # NoQA
        def decorator(txt: str) -> str:

            raw_char_list = txt.split(input_sep) if input_sep is not False else list(txt)

            filtered_char_list = [
                table[char] if char in table else char
                for char in raw_char_list
            ]

            return output_sep.join(filtered_char_list)

        return decorator
    return wrapper


@cryptor(crypt, '_')
def decrypt(txt: str) -> str:  # NoQA
    return ''


@cryptor(reverse_crypt, False, output_sep='_')
def encrypt(txt: str) -> str:  # NoQA
    return ''


def h_io() -> None:
    print(f'{'_'*50}\nWelcome to the H crypt\n')
    while True:

        cyther_int_raw: str = input('\n1 -> decrypt\n2 -> encrypt\n\t>>> ')
        try:
            cyther_int: int = int(cyther_int_raw)
            if cyther_int not in [1, 2]:
                raise Exception
        except Exception:  # NoQA
            print('Invalid input.')
            continue
        txt_input: str = input('Input text:\n\t')

        print(
            {
                1: decrypt,
                2: encrypt
            }[cyther_int](txt_input)
        )


if __name__ == '__main__':
    h_io()
