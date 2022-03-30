from collections import Counter
values=[1,4,4,5,7]
c=list(Counter(values).values())
c.sort(reverse=True)
print(c)
