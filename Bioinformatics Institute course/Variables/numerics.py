n = int(input())
base = n % 100
end = ''
if 4 < base < 20:
    end = 'ов'
else:
    base %= 10
    if 2 <= base <= 4:
        end = 'а'
    elif base != 1:
        end = 'ов'
print(n, 'программист' + end)