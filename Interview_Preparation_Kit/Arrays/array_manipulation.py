def array_manipulation(n, queries):
    arr = [0] * n

    for i in range(len(queries)):
        specs = queries[i]
        a, b, k = specs[0], specs[1], specs[2]

        for j in range(a-1, b):
            arr[j] += k
    
    max_value = max(arr)

    return max_value

def main():
    n = 10
    queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
    answer = array_manipulation(n, queries)
    return answer

if __name__ == "__main__":
    main()