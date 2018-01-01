# Mergesort Algorithm

def sort (a):
    if len(a) < 2:
        return a

    mid = len(a)//2
    left = sort(a[:mid])
    right = sort(a[mid:])

    return merge(left, right)

def merge (l, r):
    if not l or not r:
        return l or r #return the one that's not empty

    i, j, result = 0, 0, []
    for k in range(len(l) + len(r)):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1

        if i == len(l) or j == len(r):
            result += (l[i:] or r[j:]) #append the non empty list onto result
            break
        
    return result

if __name__ == "__main__":
    print(sort([2, 3, 4, 2, 3, 2, -1, 10, -15]))
