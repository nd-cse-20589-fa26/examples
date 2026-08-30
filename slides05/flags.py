import sys

arguments = sys.argv[1:]
field     = 0

while arguments and arguments[0].startswith('-'):
    match argument := arguments.pop(0):
        case '-f': field = int(arguments.pop(0))
        case '-h': usage(0)
        case _:    usage(1)

print(field)
