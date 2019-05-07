def qwe():
    print('In qwe')
    if qwe.stat == 0:
        qwe.stat = 1
        return 'return 0'
    elif qwe.stat == 1:
        qwe.stat = 2
        return 'return 1'
    elif qwe.stat == 2:
        qwe.stat = 3
        return 'return 2'
    else:
       raise StopIteration()



qwe.stat = 0

for _ in range(4):
    print(qwe())
    print('In main')

print('# =========================================== second coroutine')

def asd(end):
    print('In asd')
    asd.stat += 1
    if asd.stat >= end:
        raise StopIteration()
    return f'return {asd.stat}'


asd.stat = 0
for _ in range(11):
    print(asd(5))
    print('In main')