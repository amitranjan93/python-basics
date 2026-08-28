# backtracking
# Subsets                 → TAKE / DON'T TAKE
# Combinations            → loop + i + 1
# Permutations            → used[i]
# Permutations + duplicate → used[i] + used_values

def subsets(arr, index, current):
    if index == len(arr):
        print(current)
        return
    current.append(arr[index])
    subsets(arr,index+1,current)
    current.pop()
    subsets(arr,index+1,current)

def combinations(arr, start, current, k):
    if len(current) == k:
        print(current)
        return

    for i in range(start, len(arr)):
        current.append(arr[i])
        combinations(arr,i+1,current,k)
        current.pop()

def permutations(arr, current, used):
    if len(current) == len(arr):
        print(current)
        return
    for i in range(len(arr)):
        if not used[i]:
            current.append(arr[i])
            used[i] = True
            permutations(arr,current,used)
            used[i] = False
            current.pop()

def permutations_with_duplicates(arr, current, used):
    if len(current) == len(arr):
        print(current)
        return

    used_values = set()

    for i in range(len(arr)):
        if used[i] or arr[i] in used_values:
            continue

        used_values.add(arr[i])

        current.append(arr[i])
        used[i] = True

        permutations_with_duplicates(arr, current, used)

        used[i] = False
        current.pop()

def combination_sum(arr, start, current, target):
    if target == 0:
        print(current)
        return

    if target < 0:
        return

    for i in range(start, len(arr)):
        current.append(arr[i])
        combination_sum(arr, i, current, target - arr[i])
        current.pop()

def letter_combinations(digits,mapping, index, current):
    if index == len(digits):
        print(current)
        return
    letters = mapping[digits[index]]

    for letter in letters:
        current.append(letter)
        letter_combinations(digits,mapping,index+1,current)
        current.pop()

mapping = {
    "2": "abc",
    "3": "def"
}
letter_combinations("23",mapping,0,[])