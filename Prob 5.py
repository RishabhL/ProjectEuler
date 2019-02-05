number_list = [11, 13, 14, 16, 17, 18, 19, 20]
y = 0


def solution():
        for i in range(2520, 999999999, 2520):
            if all(i % n == 0 for n in number_list):
                return i
        return None


x = solution()
if x is None:
    print("Nothing")
else:
    print(x)
