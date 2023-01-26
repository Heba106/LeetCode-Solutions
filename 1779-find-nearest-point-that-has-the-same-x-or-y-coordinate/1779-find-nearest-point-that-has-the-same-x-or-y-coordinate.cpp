class Solution {
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) {
        int result = -1, min_distance = INT_MAX;
        for (int i = 0; i < points.size(); i++) {
            int a = points[i][0], b = points[i][1];
            if (x == a || y == b) {
                int distance = abs(x - a) + abs(y - b);
                if (distance < min_distance) {
                    min_distance = distance;
                    result = i;
                }
            }
        }
        return result;
    }
};