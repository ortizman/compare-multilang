total = 0.0
for i in range(999): # xrange is slower according 
    for j in range(1, 999):            #to my test but more memory-friendly.
        total += (i / j) * j
print total

