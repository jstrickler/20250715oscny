def doit(char, repeat):
    print(char * repeat)

doit('*', 10)
doit('_', 25)

args = ['+', 5]
doit(args[0], args[1])
doit(*args)

def junk(*, animal, country):
    print(f"{animal} is from {country}")

junk(animal="wombat", country="Australia")

args = {
    'animal': 'moose',
    'country': 'Canada',
}
junk(**args)

def add(*, x, y):
    return x + y

result = add(x=5, y=10)