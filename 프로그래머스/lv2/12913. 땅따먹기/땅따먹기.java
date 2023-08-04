class Solution {
    int solution(int[][] land) {
        int answer = 0;
        int row = land.length;
        
        for(int r = 1; r < row; r++) {
            land[r][0] += max(land[r-1][1], land[r-1][2], land[r-1][3]);
            land[r][1] += max(land[r-1][0], land[r-1][2], land[r-1][3]);
            land[r][2] += max(land[r-1][0], land[r-1][1], land[r-1][3]);
            land[r][3] += max(land[r-1][0], land[r-1][1], land[r-1][2]);
        }

        answer = max(Math.max(land[row-1][0], land[row-1][1]), land[row-1][2], land[row-1][3]);
        return answer;
    }
    
    public int max(int a, int b, int c) {
        return (Math.max(Math.max(a, b), c));
    }
}