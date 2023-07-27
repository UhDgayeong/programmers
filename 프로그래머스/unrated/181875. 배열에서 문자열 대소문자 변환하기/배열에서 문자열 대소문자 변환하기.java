import java.util.ArrayList;

class Solution {
    public String[] solution(String[] strArr) {
        ArrayList<String> answer = new ArrayList<>();
        
        for (int i = 0; i < strArr.length; i++) {
            if (i % 2 == 0) {
                answer.add(strArr[i].toLowerCase());
            } else {
                answer.add(strArr[i].toUpperCase());
            }
        }
        return answer.toArray(new String[answer.size()]);
    }
}