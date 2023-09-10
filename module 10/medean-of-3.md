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