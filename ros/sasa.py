try:
    fo = open('maa.txt')
    print(fo.read())
except FileNotFoundError:
    print('That file was not found.(')

