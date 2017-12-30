import sys
#merge sort
def merge(a,p,q,r):
    l = [sys.maxsize] * (q - p + 1 + 1);
    ri = [sys.maxsize] * (r - q + 1);
    for i in range(0,q - p + 1):
        l[i] = a[p + i]
    for j in range(0, r - q):
        ri[j] = a[q + j + 1]
    i = 0
    j = 0
    for k in range(p,r + 1):
        if l[i] <= ri[j]:
            a[k] = l[i]
            i += 1
        else:
            a[k] = ri[j]
            j += 1
def mergesort(a,p,r):
    if p < r:
        q = int((p + r) / 2)
        mergesort(a,p,q)
        mergesort(a,q + 1,r)
        merge(a,p,q,r)

a = [1,9,3,7,2,4,0,3,6,4,9,7,2,6,3,1,6,34]
print(a)
mergesort(a,0,len(a) - 1)
print(a)
