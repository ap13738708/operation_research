print 'integers from 1 to 50 divisible by 11: ',
for x in range(1, 51):
    if x % 11 == 0:
        print x,
print

print 'integers from 1 to 30 divisible by 5 or 7: ',
for x in range(1, 31):
    if (x % 5 == 0) or (x % 7 == 0):
        print x,
print

print 'integers from 1 to 30 divisible by 2 and 7: ',
x = 1
while x < 31:
    if (x % 2 == 0) and (x % 7 == 0):
        print x,
    x = x + 1
print

print 'integers from 1 to 20 not divisible by 2 nor 7: ',
x = 1
while x < 21:
    if (x % 2 != 0) and (x % 7 != 0):
        print x,
    x = x + 1
