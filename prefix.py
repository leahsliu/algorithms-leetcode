def prefixes(strings):
    i = 0
    count = 0
    possibilities = []

    while i < len(strings):
        j = 1
        while i + j < len(strings):
            w1 = strings[i]
            w2 = strings[i + j]
            l1, l2 = len(w1), len(w2)

            if w1 == w2:
                possibilities.append((w1,w2))
                count += 1
                j += 1
                continue

            if l1 >= l2:
                if w1.startswith(w2):
                    possibilities.append((w1,w2))
                    count += 1
            else:
                if w2.startswith(w1):
                    possibilities.append((w1,w2))
                    count += 1
            j += 1

        i += 1
    print("possibilities: ", possibilities)
    return count

l1 = ["back", "backdoor", "b", "abc", "a", "a", "gamma", "backgamma"]
print(prefixes(l1))
