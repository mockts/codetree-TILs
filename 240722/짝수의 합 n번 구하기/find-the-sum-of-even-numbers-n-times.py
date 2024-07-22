def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    index = 1
    results = []
    
    for _ in range(n):
        a = int(data[index])
        b = int(data[index + 1])
        index += 2
        
        if a % 2 != 0:
            a += 1
        
        total_sum = 0
        for num in range(a, b + 1, 2):
            total_sum += num
        
        results.append(total_sum)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()