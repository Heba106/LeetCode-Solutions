class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance= float('inf')
        index=-1
        for i in range (len(points)):
            if points[i][0]==x or points[i][1]==y:
                distance= abs(points[i][0]-x) + abs(points[i][1]-y)
                if distance<min_distance:
                    min_distance = distance
                    index=i
        return index