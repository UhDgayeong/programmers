class Solution {
    public int solution(int n) {
        int answer = 0;
        double sqrt = Math.sqrt(n);
        if (sqrt == (int) sqrt) {
            answer -= (int) sqrt;
        }

        for (int i = 1; i <= (int)sqrt; i++) {
            if (n % i == 0) {
                answer += i + (n / i);
            }
        }
        return answer;
    }
}