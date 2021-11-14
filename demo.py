import time

t0 = time.time()
for i in range(10000):
    print("hell")
    t1 = time.time()
    total = t1-t0
    if total > 10.0:
        break

print(total)