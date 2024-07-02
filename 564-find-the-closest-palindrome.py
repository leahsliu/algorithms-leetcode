class Solution:
    def nearestPalindromic(self, n: str) -> str:

        current = int(n)
        midP = (len(n) + 1) // 2
        possibilities = []

        if len(n) % 2 == 0:
            left = n[:midP]
            right = left[::-1]
        else:
            left = n[:midP]
            right = left[:-1][::-1]

        poss = int(left + right)
        if poss != current:
            possibilities.append((abs(current - poss), poss))
        

        for dx in [1, -1]:
            dleft = str(int(left) + dx)
            dright = dleft[::-1]
            dnum = int(dleft + dright)
            possibilities.append((abs(current - dnum), dnum))

            oddleft = str(int(left) + dx)
            oddright = oddleft[:-1][::-1]
            oddnum = int(oddleft + oddright)
            possibilities.append((abs(current - oddnum), oddnum))

        for x in range(1, 18):
            num = int("9" * x)
            if current != num:
                possibilities.append((abs(current - num), num))

            num2 = int("1" + "0" * x + "1")
            if current != num2:
                possibilities.append((abs(current - num2), num2))


        possibilities.sort()
        print(possibilities)
        return str(possibilities[0][1])