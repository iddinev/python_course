#!/usr/bin/env python3


def accepts(*args):
    def take_func(func):
        def decorator(*in_args):
            if len(args) != len(in_args):
                raise ValueError("not all input has been specified to the decorator")

            for i in range(len(args)):
                if not isinstance(in_args[i], args[i]):
                    raise TypeError("Argument {} of {} is not {}!".
                                    format(i+1, func.__name__, args[i].__name__))
            return func(*in_args)
        return decorator
    return take_func

def base_accepts(*args):
    return ', '.join([str(item) for item in args])

@accepts(str, int)
def test_accepts(*args):
    return base_accepts(*args)

def encrypt(cypher_key):
    # Do modular arithmetic on the key if key < 1 or > 26.
    cypher_key = cypher_key % 26
        def decorator():
            clear_text = func()

            return func(*in_args)
    return decorator


@encrypt(2)
def test_encrypt():
    return 'a b c d'
