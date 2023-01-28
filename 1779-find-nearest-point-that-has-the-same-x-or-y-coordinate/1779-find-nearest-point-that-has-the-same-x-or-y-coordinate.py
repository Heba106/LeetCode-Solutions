class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance= float('inf')
        index=-1
        for i,p in enumerate (points):
            if p[0]==x or p[1]==y:
                distance= abs(p[0]-x) + abs(p[1]-y)
                if distance<min_distance:
                    min_distance = distance
                    index=i
        return index