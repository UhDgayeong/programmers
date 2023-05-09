import java.util.*;

class Solution {
    public String solution(int a, int b) {
        String answer = "";
        int days = -1;
        Map<Integer, Integer> map = new HashMap<>() {{
            put(1, 31);
            put(2, 29);
            put(3, 31);
            put(4, 30);
            put(5, 31);
            put(6, 30);
            put(7, 31);
            put(8, 31);
            put(9, 30);
            put(10, 31);
            put(11, 30);
            put(12, 31);
        }};
        
        String[] dates = {"FRI","SAT","SUN","MON","TUE","WED","THU"};
        
        for (int i = 1; i < a; i++) {
            days += map.get(i);
        }
        days += b;
        
        return dates[days % 7];
    }
}
