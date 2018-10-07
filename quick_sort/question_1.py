def quick_sort(list_values, lo, hi):
    if lo<hi:
        pivot = partition(list_values, lo, hi)
        quick_sort(list_values, pivot+1, hi)
        quick_sort(list_values, lo, pivot-1)

def partition(list_values, lo, hi):
    pivot = list_values[hi]
    i = lo
    for j in range(lo, hi):
        if list_values[j] < pivot:
            tmp = list_values[j]
            list_values[j] = list_values[i]
            list_values[i] = tmp
            i += 1
    tmp = list_values[i]
    list_values[i] = list_values[hi]
    list_values[hi] = tmp
    return i


if __name__ == '__main__':
    example_list = [12, 3, 23, 1, 99, 2, 44]
    quick_sort(example_list, 0, 6)
    print(example_list)  

