def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    numbers = [int(input("Enter a number: ")) for _ in range(3)]
    factorials = [factorial(num) for num in numbers]
    total = sum(factorials)
    print("Factorials:", factorials)
    print("Sum of factorials:", total)

if __name__ == "__main__":
    main()
