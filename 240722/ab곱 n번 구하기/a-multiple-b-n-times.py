def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    results = []
    
    index = 1
    for _ in range(n):
        a = int(data[index])
        b = int(data[index + 1])
        index += 2
        
        product = 1
        for num in range(a, b + 1):
            product *= num
        
        results.append(product)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()