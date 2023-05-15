class Solution {
    public int solution(String s) {
        int answer = 1;
        char[] arr = s.toCharArray();
        int idx = 0;
        int len_arr = arr.length;
        char first = arr[0];
        int cnt_first = 0;
        int cnt_other = 0;
        
        for (char a: arr) {
            if (cnt_first == 0) {
                first = a;
            }
            
            if (a == first) {
                cnt_first += 1;
            }
            else {
                cnt_other += 1;
            }
            
            if (cnt_first == cnt_other) {
                cnt_first = 0;
                cnt_other = 0;
                if (idx != len_arr - 1)
                    answer += 1;
            }
            idx += 1;
        }
        
        return answer;
    }
}