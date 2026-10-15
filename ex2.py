def merge(left, right):
    result = []
    i = 0
    j = 0
    comparisons = 0

    while i < len(left) and j < len(right):
        comparisons += 1

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result, comparisons


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    left, c1 = merge_sort(arr[:mid])
    right, c2 = merge_sort(arr[mid:])

    merged, c3 = merge(left, right)

    return merged, c1 + c2 + c3


prices = list(map(int, input("Enter product prices: ").split()))

sorted_prices, comparisons = merge_sort(prices)

print("Sorted Product Prices:", sorted_prices)
print("Number of Comparisons:", comparisons)