a = 1
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def printall():
    print {"a":a,
            "b":b,
            "c":c,
            "d":d,
            "e":e,
            "f":f,
            "g":g,
            "h":h}

b = 107900
c = 107900 + 17000
while True:
    f = 1
    d = 2

    if not is_prime(b):
        f = 0

#    while True:
#        e = 2
#        printall()
##        while True:
##            if d*e == b:
##                f = 0
##            e += 1
##            g = e-b
##            if e == b:
##                break
#        e = b
#        d += 1
#        g = d - b
#        if g == 0:
#            break
    if f == 0:
        h += 1
    if b != c:
        b += 17
    else:
        print h
        exit()



