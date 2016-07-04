#!/usr/bin/env python3


#  def decorator_var(var):
    #  def decorator_func(func):
        #  def decorated(a, b):
            #  print('a, b ++{}'.format(var))
            #  a += var
            #  b += var
            #  return func(a, b)
        #  return decorated
    #  return decorator_func


#  def bare_func(a, b):
    #  print('a+b = {}'.format(a+b))


#  @decorator_var(2)
#  def test_func(a, b):
    #  #  print('a+b = {}'.format(a+b))
    #  return bare_func(a, b)


def base_accepts(*args):
    print('args are: ', args)


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


@accepts(str, int)
def test_accepts(*args):
    return base_accepts(*args)
