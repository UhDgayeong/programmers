class Solution {
    public int solution(String my_string) {
        int answer = 0;
        char[] arr = my_string.toCharArray();
        for (int i = 0; i < my_string.length(); i++) {
            if (Character.isDigit(arr[i])) {
                answer += Character.getNumericValue(arr[i]);
            }
        }
        return answer;
    }
}