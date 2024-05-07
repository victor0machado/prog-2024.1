while True:
    n = int(input())
    if n == 0:
        break

    nums = [int(i) for i in input().split()]
    print("Mary won", nums.count(0), "times and John won", nums.count(1), "times")
