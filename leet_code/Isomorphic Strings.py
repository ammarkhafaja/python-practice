# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

def isIsomorphic(self, s: str, t: str) -> bool:
    ress={}
    rett={}
    for ss,tt in zip(s,t):
        ress[ss]=ress.get(ss,[])
        rett[tt]=rett.get(tt,[])
        if tt not in ress[ss]:
            ress[ss].append(tt)
            if len(ress[ss])>1:
                return False
        if ss not in rett[tt]:
            rett[tt].append(ss)
            if len(rett[tt])>1:
                return False
    return True