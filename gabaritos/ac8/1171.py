n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))

unicos = list(set(nums))
unicos.sort()

for num in unicos:
    print(num, "aparece", nums.count(num), "vez(es)")
