# Randomized QuickSort
```
Randomized_QuickSort(A, low, high)
    if low < high
        pivotIndex = Randomized_Partition(A, low, high)
        Randomized_QuickSort(A, low, pivotIndex-1)
        Randomized_QuickSort(A, pivotIndex+1, high)

Randomized_Partition(A, low, high)
    randomIndex = Random(low, high) // Generate a random number between low and high
    swap A[randomIndex] and A[high] // Swap the random element with the last element
    return Partition(A, low, high) // Use regular partitioning algorithm

Partition(A, low, high)
    pivot = A[high]
    i = low
    for j = low to high-1
        if A[j] <= pivot
            swap A[i] and A[j]
            i = i + 1
    swap A[i] and A[high]
    return i

```
# Median of 3
```
function quicksort(array, low, high)
    if low < high
        pivotIndex = medianOfThree(array, low, high)
        pivotIndex = partition(array, low, high, pivotIndex)
        
        quicksort(array, low, pivotIndex - 1)
        quicksort(array, pivotIndex + 1, high)
    end if
end function
```
```
function medianOfThree(array, low, high)
    mid = (low + high) / 2

    if array[low] > array[high]
        swap(array[low], array[high])
    end if
    
    if array[low] > array[mid]
        swap(array[low], array[mid])
    end if

    if array[mid] > array[high]
        swap(array[mid], array[high])
    end if

    return mid
end function
```
```
function partition(array, low, high, pivotIndex)
    pivotValue = array[pivotIndex]
    swap(array[pivotIndex], array[high])  // Move pivot to end
    
    storeIndex = low
    
    for i = low to high - 1
        if array[i] <= pivotValue
            swap(array[i], array[storeIndex])
            storeIndex = storeIndex + 1
        end if
    end for
    
    swap(array[storeIndex], array[high])  // Move pivot to its final position
    
    return storeIndex
end function
```
```
function swap(a, b)
    temp = a
    a = b
    b = temp
end function
```