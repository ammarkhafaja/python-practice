def lengthOfLastWord(self, s: str) -> int:
    listy=s.split()
    return len(listy[-1])