
def longest(arr):
    k = 0
    for i in range(0, len(arr)):
        if len(arr[i]) > k:
            k = len(arr[i])
            longer = arr[i]
    print(longer)

longest(["Anele", " is", " a ", "cute", "gangster"])
