if __name__ == '__main__':
    testString = "Welcome to Python training!"
    print(testString)
    print(len(testString))

    # in clause in string: to find the substring
    print("Python" in testString)
    # case sensitive language
    print("python" in testString)
    # How to get substrings based on their positions
    print(testString[3:8])
    print(testString[11:])
    print(testString[:10])
    #print(testString[:-1])

    print(testString.upper())
    print(testString.lower())