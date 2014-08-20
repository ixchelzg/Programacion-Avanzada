print "Hello, World!"
try:
    mode=int(raw_input('Input:'))
except ValueError:
    print "Not a number"