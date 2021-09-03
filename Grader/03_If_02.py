std1 = input().split()
std2 = input().split()

if (std1[2] == 'A' and std1[3] in "ABC" and std1[4] in "ABC") and not(std2[2] == 'A' and std2[3] in "ABC" and std2[4] in "ABC"):
    print(std1[0])
elif not(std1[2] == 'A' and std1[3] in "ABC" and std1[4] in "ABC") and (std2[2] == 'A' and std2[3] in "ABC" and std2[4] in "ABC"):
    print(std2[0])
elif (std1[2] == 'A' and std1[3] in "ABC" and std1[4] in "ABC") and (std2[2] == 'A' and std2[3] in "ABC" and std2[4] in "ABC"):
    if float(std1[1]) > float(std2[1]):
        print(std1[0])
    elif float(std1[1]) < float(std2[1]):
        print(std2[0])
    elif (std1[3]) < (std2[3]):
        print(std1[0])
    elif (std1[3]) > (std2[3]):
        print(std2[0])
    elif (std1[4]) < (std2[4]):
        print(std1[0])
    elif (std1[4]) > (std2[4]):
        print(std2[0])
    else:
        print("Both")
else:
    print("None")