# класс, фильтрующий по нескольким функциям

class multifilter():
    def judge_half(self, pos, neg):
        return pos >= neg

    def judge_any(self, pos, neg):
        return pos >= 1

    def judge_all(self, pos, neg):
        return neg == 0

    def __next__(self):
        while self.i < self.end:
            element = self.iterable[self.i]
            pos = sum(func(element) for func in self.funcs)
            neg = sum(not func(element) for func in self.funcs)
            if self.judge(self, pos, neg):
                self.i += 1
                return element
            else:
                self.i += 1
        else:
            raise StopIteration

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        self.i = 0
        self.end = len(self.iterable)

    def __iter__(self):
        return self


def mul2(x):
    return len(x) > 1

def mul3(x):
    return int(x) % 3 == 0

def mul5(x):
    return x[0] == '1'


a = [str(i) for i in range(31)] # [0, 1, 2, ... , 30]

print(a)

print(list(multifilter(a, mul2, mul3, mul5))) 
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half))) 
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all))) 
# [0, 30]