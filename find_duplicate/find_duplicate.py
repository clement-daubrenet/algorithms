
def find_duplicates(nums):
    """
    Find duplicates using cycle detection ("hare and tortoise" algorithm).
    """

    tortoise = nums[0]
    hare = nums[0]

    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    pointer_1 = nums[0]
    pointer_2 = tortoise

    while pointer_1 != pointer_2:
        pointer_1 = nums[pointer_1]
        pointer_2 = nums[pointer_2]

        if pointer_1 == pointer_2:
            break

    return pointer_1


if __name__ == '__main__':
    L = [3, 1, 3, 4, 2]
    print(find_duplicates(L))
