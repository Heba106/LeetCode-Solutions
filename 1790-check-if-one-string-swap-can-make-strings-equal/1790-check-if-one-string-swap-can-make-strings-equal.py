class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        counter=0
        index=[]
        for i, a in enumerate(s1):
            if counter<=2:
                if a!= s2[i]:
                    counter+=1
                    index.append(i)
            else:
                return False
            
        if counter==2:
            s1 = list(s1)
            s1[index[0]], s1[index[1]]=s1[index[1]], s1[index[0]]
            s1=''.join(s1)
            print(s1)
        return True if s1==s2 else False
        