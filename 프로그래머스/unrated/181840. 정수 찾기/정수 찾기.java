import java.util.*;

class Solution {
    public int solution(int[] num_list, int n) {
        int answer = 0;
        List<Integer> list = new ArrayList<>();
        for (int i : num_list) {
            list.add(i);
        }
        if (list.contains(n)) { answer = 1; }
        return answer;
    }
}