def array_manipulation(n, queries):
    arr = [0] * n
    
    for i in range(len(queries)):
        
        specs = queries[i]
        a, b, k = specs[0], specs[1], specs[2]

        arr[a - 1: b] = map((k).__add__, arr[a - 1: b])

    max_val = 0
    for item in arr:
        if item > max_val:
            max_val = item
    
    return max_val

def main():
    n = 10
    queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
    answer = array_manipulation(n, queries)
    print(answer)

if __name__ == "__main__":
    main()