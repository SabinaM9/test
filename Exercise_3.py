# return reversed string without build-in libraries

def get_reverse_str(name: str):
    reversed = name[::-1]
    return reversed

print(get_reverse_str('Paul Ho'))

def get_reverse_str_alternative(name: str):
    i = -1
    reversed = ""
    while len(reversed) < len(name):
        reversed = reversed + name[i]
        i += -1
    return reversed

print(get_reverse_str_alternative('Paul Ho'))
