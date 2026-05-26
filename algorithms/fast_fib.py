memo = {} 

def fast_fib(n):
    # 1. Check the notebook
    if n in memo:
        return memo[n]
    
    # 2. Base cases
    if n <= 1:
        return n
    
    # 3. Calculate and save 
    memo[n] = fast_fib(n - 1) + fast_fib(n - 2)
    return memo[n]

def main():
    num = int(input("Enter a number: "))
    # We  pass the number, not the memo
    result = fast_fib(num)
    print(result)

if __name__ == "__main__":
    main()