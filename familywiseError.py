alpha = 0.05
n = [5, 10]

for i in n:
    familyerror = 1-(1-alpha)**i
    print("for {} number of tests done, the familywise error is {}".format(i, familyerror))