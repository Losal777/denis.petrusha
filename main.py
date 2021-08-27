def func(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)
    print(arg5)
    print(arg6)
    print(arg7)


l = ['mum', 'grandfather', 'brother', 'queue', 'clock', 'basketball', 'fox']

func(*l)


def func(na):
    N = len(na)
    c = [0] * N

    # Index of string with
    # maximum unique characters
    m = 0

    # Iterate through all strings
    for j in range(N):

        # Array indicating any alphabet
        # included or not included
        character = [False] * 26

        # count number of unique
        # alphabets in each string
        for k in range(len(na[j])):
            x = ord(na[j][k]) - ord('A')

            if ((na[j][k] != ' ') and (character[x] == False)):
                c[j] += 1
                character[x] = True

            # keep track of maximum
            # number of alphabets
            if (c[j] > c[m]):
                m = j

    # print result
    print(na[m])


# Driver code
na = ["BOB", "A AB C JOHNSON", "ANJALI",
      "ASKRIT", "ARMAN MALLIK"]
func(na)

