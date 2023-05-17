import java.util.*;

class Solution {
    public static boolean isInteger(String strValue) {
    try {
      Integer.parseInt(strValue);
      return true;
    } catch (NumberFormatException ex) {
      return false;
    }
  }
    public int solution(String s) {
        String answer = "";
        char arr[] = s.toCharArray();
        String tmp = "";
        HashMap<String, String> map = new HashMap<>();
        map.put("zero", "0");
        map.put("one", "1");
        map.put("two", "2");
        map.put("three", "3");
        map.put("four", "4");
        map.put("five", "5");
        map.put("six", "6");
        map.put("seven", "7");
        map.put("eight", "8");
        map.put("nine", "9");
        
        for (int i = 0; i < arr.length; i++) {
            if (!isInteger(Character.toString(arr[i]))) {
                tmp += Character.toString(arr[i]);
                if (map.containsKey(tmp)) {
                    answer += map.get(tmp);
                    tmp = "";
                }
            }
            
            else {
                if (!tmp.matches("")) {
                    if (map.containsKey(tmp)) {
                        answer += map.get(tmp);
                        tmp = "";
                    }
                }
                answer += Character.toString(arr[i]);
            }
            
        }
        return Integer.parseInt(answer);
    
    }
}