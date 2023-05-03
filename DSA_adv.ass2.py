#Question1

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        if arr[mid] < x:
            low = mid + 1
 
        elif arr[mid] > x:
            high = mid - 1
 
        else:
            return mid
 
    return -1
 
 
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
result = binary_search(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
Element is present at index 3

#Question2 

def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	L = [0] * (n1)
	R = [0] * (n2)

	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	i = 0	 
	j = 0	 
	k = l	 

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

def mergeSort(arr, l, r):
	if l < r:

		m = l+(r-l)//2

		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)


arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
	print("%d" % arr[i],end=" ")

mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
	print("%d" % arr[i],end=" ")


#Question3 

def partition(array, low, high):
     
    pivot = array[high]
 
    i = low - 1
 
    for j in range(low, high):
        if array[j] <= pivot:
 
            i = i + 1

            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    return i + 1
 
def quicksort(array, low, high):
    if low < high:

        pi = partition(array, low, high)
 
        quicksort(array, low, pi - 1)
 
        quicksort(array, pi + 1, high)

if __name__ == '__main__':
    array = [10, 7, 8, 9, 1, 5]
    N = len(array)
 
    quicksort(array, 0, N - 1)
    print('Sorted array:')
    for x in array:
        print(x, end=" ")


#Question4

def insertionSort(arr):
     
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 
 
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])


#Question 5 

def compare(a, b):
    return ((a < b) - (a > b))


def sort_string(arr):
        temp = ""
        n = len(arr)
        for i in range(n-1):
            for j in range(i+1, n):
                if compare(arr[j], arr[i]) > 0:
                    temp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = temp
        print("String in sorted order are: ",arr)

arr = ["hey", "bye", "my", "toy", "roy"]

sort_string(arr)    

	
