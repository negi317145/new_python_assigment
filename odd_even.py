odds = (n for n in range(1,102) if n % 2)
for n in odds:
    print(n, 'odd number:',)
evens = (n for n in range(1,102) if n % 2 == 0)
for n in evens:
    print('even number:',n)