def function(choos):
    if choos == 2:
        return 1,2
    if choos == 1:
        return 1
val = function(1)
if len(val) == 2:
    print(f"{val[0]} {val[1]}")
if len(val) == 1:
    print(f"{val[0]}")