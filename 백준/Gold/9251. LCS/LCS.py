str1 = ' ' + input()
str2 = ' ' + input()
lcs = [[0 for _ in range(len(str2))] for _ in range(len(str1))]
for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            lcs[i][j] = 1 + lcs[i-1][j-1]
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
print(lcs[-1][-1])