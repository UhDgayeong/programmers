import java.util.*;

class Solution {
    public ArrayList solution(String s) {
        ArrayList<Integer> answer = new ArrayList<>();
        HashMap<Character, Integer> map = new HashMap<>();
        char[] str = s.toCharArray();
        int idx = 0;
        for (char st : str) {
            if (map.containsKey(st)) {
                answer.add(idx - map.get(st));
            }
            else {
                answer.add(-1);
            }
            map.put(st, idx);
            idx += 1;
        }
        return answer;
    }
}