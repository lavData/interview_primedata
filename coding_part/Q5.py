import copy


''' My opinion: Two arrays have been sorted, so I just count from two arrays
                by ascending order. Length of arr1, arr2 is n1, n2 .So: 
                If n1 + n2 is odd, the median is element has index (n1 + n2) / 2. 
                Else, the median index is avagrage (n1 + n2) / 2 - 1 and (n1 + n2) / 2.

    My algorithm:
    1. Assign i ,j = 0. n1 = length(arr1), n2 = length(arr2). result = 0. O(1)
    2. If n1 + n2 is odd: 
        Create a loop with (n1 + n2) // 2 loops. 
        2.1 If i and j not equal n1 and n2. I will compare arr1[i] and arr2[j].
            If arr1[i] < arr2[j] -> The present result is arr1[i], i += 1
            Else -> the present result is arr1[j],  j += 1
        2.2 If i = n1 and i not = n2 yet. -> The present result is arr2[j], j += 1
        2.3 Else -> The present result is arr1[i], i += 1

        Finish loop, return the present result.

        => The complexity is O(1/2 (n1 + n2))
    3. Else:
        Same step 2. But have temp variable to keep value of index (n + m) // 2 - 1.

        Finish loop, return the present (result + temp) / 2

        => O(1/2 (n1 + n2))

    => The complexity is O(n1 + n2)

'''


def median_two_sorrted_arrays(arr1, arr2):
    
    i = 0
    j = 0

    n1 = len(arr1)
    n2 = len(arr2)

    result = 0

    if (n1 + n2) % 2 == 1:
        for k in range((n1 + n2) // 2 + 1):
            if i != n1 and j != n2:
                if arr1[i] < arr2[j]:
                    result = arr1[i]
                    i += 1
                else:
                    result = arr2[j]
                    j += 1
            elif j != n2:
                result = arr2[j]
                j += 1
            else:
                result = arr1[i]
                i += 1
        return result
    else:
        for k in range((n1 + n2) // 2 + 1):
            temp = copy.deepcopy(result)
            if i != n1 and j != n2:
                if arr1[i] < arr2[j]:
                    result = arr1[i]
                    i += 1
                else:
                    result = arr2[j]
                    j += 1
            elif j != n2:
                result = arr2[j]
                j += 1
            else:
                result = arr1[i]
                i += 1
        return (temp + result) / 2

if __name__ == '__main__':
    arr1 = list(map(int, input("nums1: ").split()))
    arr2 = list(map(int, input("nums2: ").split()))

    print("Median of merged array is", median_two_sorrted_arrays(arr1, arr2))
