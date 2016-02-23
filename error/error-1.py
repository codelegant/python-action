import sys

try:
    f = open('data.json')
    s = f.readline()
    i = int(s.strip())
except IOError as err:
    print('I/O error:{0}'.format(err))
except ValueError:
    print('Could not convert data ot an integer.')
except:
    print('Unexpected error:', sys.exc_info()[0])
    raise
else:
    print(i)
