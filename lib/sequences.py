def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    elif length == 2:
        print([0, 1])
        return
    
    fib_seq = [0, 1]
    for i in range(2, length):
        next_term = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_term)
    
    print(fib_seq)

