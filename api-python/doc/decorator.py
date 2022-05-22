# https://www.youtube.com/watch?v=TaZGQXWFsf4
# https://flask-restful.readthedocs.io/en/latest/extending.html
# https://towardsdatascience.com/using-class-decorators-in-python-2807ef52d273

# wrapper

from pdb import set_trace

# import pdb; pdb.set_trace()

# ypython (Terminal)
# from inspect import getargvalues

# decorator em forma de classe
# class uppercase(object):
#     def __init__(self, f):
#         print("Funcionalidades executadas no metod __init__")
#         self.f = f

#     def __call__(self, *args, **kwargs):
#         self.f(args[0].upper())

# @uppercase
# def nome(nome):
#     print("Nome: %s" % nome)


# nome("Fred")

########################################
# Decorater como função
# def uppercase(func):
#     def uppercase(*args, **kwargs):  # def uppercase(nome): # print(f"{nome}")
#         print("before function")
#         # print(f"Chamando funcao: {func.__name__} | args: {args}, | kwargs: {kwargs}")
#         # print("Chamando funcao: %s()" % (func.__name__))
#         return func(*args, **kwargs)

#     return uppercase


# @uppercase
# def nome(nome):
#     print("Nome: %s" % nome)


# nome("Fred")

########################################
def decorador(args_decorator):
    print(args_decorator)
    # Parametros do decorador
    def decorador_real(func):
        print(func.__name__)
        # Recebera função
        def execute_function(*args_function):
            print(args_function)
            # Executar a função
            pass

        return execute_function

    return decorador_real


@decorador("Igor")
def soma(x, y):
    return x + y


soma(2, 2)
