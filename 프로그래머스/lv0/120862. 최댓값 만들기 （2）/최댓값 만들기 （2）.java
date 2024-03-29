import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        Arrays.sort(numbers);
        if (numbers.length >= 3) {
            int num1 = numbers[0] * numbers[1];
            int num2 = numbers[numbers.length - 1] * numbers[numbers.length - 2];
            answer = (num1 >= num2) ? num1 : num2;
        } else {
            answer = numbers[0] * numbers[1];
        }
        return answer;
    }
}