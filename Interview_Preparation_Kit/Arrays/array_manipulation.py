def array_manipulation(n, queries):
    arr = [0]*n
    
    for i in queries:
        arr[i[0] - 1] += i[2]
        if i[1] != len(arr):
            arr[i[1]] -= i[2]

    maxval = 0
    itt = 0
    for q in arr:
        itt += q
        if itt > maxval:
            maxval = itt

    return maxval

def main():
    n = 10
    queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
    answer = array_manipulation(n, queries)
    print(answer)

if __name__ == "__main__":
    main()