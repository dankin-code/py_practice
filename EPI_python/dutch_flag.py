red, white, blue = range(3)
def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    # first pass: group elements small than pivot
    for i in range(len(A)):
        # look for a smaller element
        for j in range(i+1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    # second pass: group elements larger than pivot
    for i in reversed(range(len(A))):
        # look for a larger element. Stop when we reach an element less than
        # pivot, since first pass has move them to the start of A
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break
