

d = float(input('Type the number you want divide: '))
q = float(input('Type the coeficient of operation: '))
try:
    assert q > 0
except:
    print('Error. Devide by 0.')
    exit(0)

try:
    total = d // q
    remainder = d % q
finally:
    print('The result is: {}'.format(total))
    if(d % q > 0):
        print('The remainder of the operation is: {}'.format(remainder))

#teste
# print(((225 * 100) / 197) - 100)
