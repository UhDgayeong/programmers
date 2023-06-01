class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int len_a = Integer.toString(a).length();
        int len_b = Integer.toString(b).length();
        
        answer = (a * (int)Math.pow(10, len_b) + b > b * (int)Math.pow(10, len_a) + a) ? a * (int)Math.pow(10, len_b) + b : b * (int)Math.pow(10, len_a) + a;
        return answer;
    }
}