# Quicksort Algorithm

# Average Case Time: O(N log N)
# Worst Case Time: O(N^2)

# Worst Case Space: O(log N)   (stack space)
import random

class QuickSort:            
    #Static method called to sort
    def sort(a, lo = 0, hi = None):
        QuickSort.shuffle(a)
        if hi is None:
            hi = len(a) - 1
        def _sort (a, lo, hi):
            if hi <= lo:
                return
            j = QuickSort.partition(a, lo, hi)
            _sort(a, lo, j-1)
            _sort(a, j+1, hi)

        return _sort(a, lo, hi)

    # partition subarray a[lo..hi] s.t. a[lo..j-1] <= a[j] <= a[j+1..hi]
    def partition(a, lo, hi):
        pivot = lo
        for i in range(lo + 1, hi + 1):
            if a[i] <= a[lo]:
                pivot += 1
                a[i], a[pivot] = a[pivot], a[i]
        a[pivot], a[lo] = a[lo], a[pivot]
        return pivot

    #Knuth Shuffle algorithm to ensure quicksort works well
    def shuffle(a):
        for i in range(len(a)):
            j = random.randrange(i, len(a))
            a[i], a[j] = a[j], a[i]
