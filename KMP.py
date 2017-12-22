#build array to show how many suffix that same as prefix at the position
def lps(s):
    arr = [0] * len(s)

    j = 0;
    i = 1;
    for i in range(1,len(s)):
        if s[i] == s[j]:
            arr[i] = j + 1
            j = j + 1
        else :
            j = arr[j - 1]
            while j > 0:
                if s[j] == s[i]:
                    arr[i] = j + 1
                    j = j + 1
                    break
                else :
                    j = arr[j - 1]
            if j == 0 :
                arr[i] = 0
    print(arr)
    return arr
#build kmp find substring position in string
def KMP(s,x):
    isHasSub = False
    pos = -1
    j = 0
    i = 0
    pattern = lps(x)

    while i < len(s):
        if s[i] == x[j]:
            if j == len(x) - 1:
                isHasSub = True
                pos = i - len(x) + 1
                break
            i = i + 1
            j = j + 1

        else:
            if j == 0 :
                i = i + 1
            else :
                j = pattern[j - 1]

    if isHasSub :
        return pos
    return -1

s = "abxabcabcaby"
x = "abcaby"

print(s)
print(x)

print(KMP(s,x))
