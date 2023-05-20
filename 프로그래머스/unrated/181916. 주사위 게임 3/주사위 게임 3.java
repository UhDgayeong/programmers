import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        int arr[] = {a, b, c, d};
        
        for (int num : arr) {
            if (map.containsKey(num)) {
                map.put(num, map.get(num) + 1);
            }
            else {
                map.put(num, 1);
            }
        }
        
        int len_keys = map.size();
        if (len_keys == 1) {
            answer = 1111 * a;
        }
        else if (len_keys == 2) {
            int p = 0;
            int q = 0;
            int firstVal = 0;
            
            for (Map.Entry<Integer, Integer> entrySet : map.entrySet()) {
                firstVal = entrySet.getValue();
                break;
            }
            
            if (firstVal == 2) {
                for (Map.Entry<Integer, Integer> entrySet : map.entrySet()) {
                    if (p == 0) {
                        p = entrySet.getKey();
                    } else {
                        q = entrySet.getKey();
                    }
                }
                answer = (p + q) * Math.abs(p - q);
            } else {
                for (Map.Entry<Integer, Integer> entrySet : map.entrySet()) {
                int val = entrySet.getValue();
                if (val == 1) {
                    q = entrySet.getKey();
                } else {
                    p = entrySet.getKey();
                }
            }
            answer = (int)Math.pow(10 * p + q, 2);
            }
        }
        else if (len_keys == 3) {
            int tmp = 1;
            for(Map.Entry<Integer, Integer> entrySet : map.entrySet()) {
                int val = entrySet.getValue();
                if (val == 1) {
                    tmp *= entrySet.getKey();
                }
            }
            answer = tmp;
        }
        else {
            int min = 10;
            for (int i : arr) {
                min = Math.min(i, min);
            }
            answer = min;
        }
        
        return answer;
    }
}