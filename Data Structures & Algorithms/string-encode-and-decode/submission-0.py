class Solution:

    def encode(self, strs):
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):

            # Find the '#'
            j = i
            while s[j] != '#':
                j += 1

            # Get length
            length = int(s[i:j])

            # Move after '#'
            i = j + 1

            # Get the string
            result.append(s[i:i + length])

            # Move to next string
            i = i + length

        return result