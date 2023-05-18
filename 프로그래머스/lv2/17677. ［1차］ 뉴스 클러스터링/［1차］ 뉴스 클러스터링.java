import java.util.HashMap;
import java.util.Iterator;

class Solution {
    public int solution(String str1, String str2) {
        float answer = 0;
        int tmp = 0;
        int arr1Cnt = 0;
        int arr2Cnt = 0;
        HashMap<String, Integer> mapA = new HashMap<>();
        HashMap<String, Integer> mapB = new HashMap<>();
        String pattern = "^[a-z]*$";
        
        for (int i = 0; i < str1.length() - 1; i++) {
            String str = str1.substring(i, i+2).toLowerCase();
            if (str.matches(pattern)) {
                if (mapA.containsKey(str)) {
                    mapA.put(str, mapA.get(str) + 1);
                        
                } else {
                    mapA.put(str, 1);
                }
                arr1Cnt += 1;
            }
        }
        for (int i = 0; i < str2.length() - 1; i++) {
            String str = str2.substring(i, i+2).toLowerCase();
            if (str.matches(pattern)) {
                if (mapB.containsKey(str)) {
                    mapB.put(str, mapB.get(str) + 1);
                        
                } else {
                    mapB.put(str, 1);
                }
                arr2Cnt += 1;
            }
        }
        
        Iterator iteratorA = (mapA.keySet().iterator());
        while (iteratorA.hasNext()) {
            String key = (String)iteratorA.next();
            if (mapB.containsKey(key)) {
                tmp += (mapA.get(key) < mapB.get(key)) ? mapA.get(key) : mapB.get(key);
            }
        }
        
        answer = (float)tmp / (arr1Cnt + arr2Cnt - tmp);
        if (Float.isNaN(answer)) {
            answer = 1;
        }
        
        return (int)(answer * 65536);
    }
}