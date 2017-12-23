# a i u e o

def isVow(s):
    if s == "a" or s == "i" or s == "u" or s == "e" or s == "o":
        return True
    return False
def classifyStrings(s):
    #bad
    vow = []
    cons = []
    onlyVow = []
    onlyCons = []
    for i in range(0, len(s)):
        if isVow(s[i]) :
            vow.append(i)
            onlyVow.append(i)
        else:
            if s[i] == "?":
                vow.append(i)
                cons.append(i)
            else:
                cons.append(i)
                onlyCons.append(i)
    print(onlyVow)
    print(onlyCons)
    print(vow)
    print(cons)
    #write method to traverse from top to bot if array contains 3 vovals consecutive or 5 consecutive consonants
    #if it has then return "bad"
    #if isContain ? then return "mixed"
    vo = 1
    for i in range(1,len(onlyVow)):
        if onlyVow[i] == onlyVow[i - 1] + 1:
            vo += 1
            if vo == 3 :
                return "bad"
        else :
            vo = 1
    vo = 1
    for i in range(1,len(onlyCons)):
        if onlyCons[i] == onlyCons[i - 1] + 1:
            vo += 1
            if vo == 5 :
                return "bad"
        else :
            vo = 1

    vo = 1
    hs = set([])
    isQuestionRepeat = False
    isBad = False
    for i in range(1,len(vow)):
        if vow[i] == vow[i - 1] + 1:
            vo += 1
            if vo == 3 :
                isBad = True
                for i in range(2,-1,-1):
                    if s[vow[i]] == "?":
                        hs.add(vow[i])
                vo = 1
        else :
            vo = 1
    co = 1
    for i in range(1,len(cons)):
        if cons[i] == cons[i - 1] + 1:
            co += 1
            if co == 5 :
                isBad = True
                for i in range(2,-1,-1):
                    if s[cons[i]] == "?":
                        if cons[i] in hs:
                            isQuestionRepeat = True
                co = 1
        else :
            co = 1

    if isBad :
        if isQuestionRepeat:
            return "bad"
        return "mixed"
    return "good"

print(classifyStrings("???"))
