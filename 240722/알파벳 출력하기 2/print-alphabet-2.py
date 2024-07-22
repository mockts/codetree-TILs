def main():
    import sys
    input = sys.stdin.read
    N = int(input().strip())
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = 0
    
    for i in range(N):
        line = ""
        for j in range(N - i):
            line += alphabet[index] + " "
            index = (index + 1) % 26
        print(" " * i * 2 + line.rstrip())

if __name__ == "__main__":
    main()