import java.util.HashMap;

class Solution {
    public int solution(int[][] lines) {
        int answer = 0;
        HashMap<Integer, Integer> hm = new HashMap<>();
        
        for (int[] line: lines) {
            for (int i = line[0] + 1; i <= line[1]; i++) {
                if (hm.containsKey(i)) {
                    hm.put(i, hm.get(i) + 1);
                } else {
                    hm.put(i, 1);
                }
    
            }
        }
        
        for (int key: hm.keySet()) {
            int val = hm.get(key);
            if (val >= 2) {
                answer += 1;
            }
        }
        
        return answer;
    }
}