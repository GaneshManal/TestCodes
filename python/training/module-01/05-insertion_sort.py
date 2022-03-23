def insertion_sort():
    arr=[2,4,3,1]
    for i in range(len(arr)):
        for j in range(i-1,-1,-1):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]    
        print(arr)

if __name__ == "__main__":
    insertion_sort()
