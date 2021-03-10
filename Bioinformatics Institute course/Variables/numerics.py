n = int(input())
base = n % 100
end = 'a'
if 4 < base < 20:
    end = 'ов'
elif base % 10 == 1:
    end = ''
print(n, 'программист' + end)