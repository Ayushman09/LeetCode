def partitionLabels(self, s: str) -> List[int]:
        # Store index of the last occurence of every character in the string
        last = {c: i for i, c in enumerate(s)}
        output = []
        # Create three variables as following:
        # 1. start: Starting index of substring
        # 2. allChars: Set representing all characters in the current substring
        # 3. finishedChars: Set representing finished characters in the current substring
        start, allChars, finishedChars = 0, set(), set()
        for i, c in enumerate(s):
            if(c not in allChars):
                allChars.add(c)
            if(i == last[c]):
                finishedChars.add(c)
            # We have obtained a partition when all characters are finished
            if(len(allChars) == len(finishedChars)):
                output.append(i - start + 1)
                start, allChars, finishedChars = i + 1, set(), set()
        return output