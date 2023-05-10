import java.util.*;

public class Solution {
    public ArrayList solution(int []arr) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        answer.add(arr[0]);
        int last_add = arr[0];
        
        for (int a : arr) {
            if (a != last_add) {
                answer.add(a);
                last_add = a;
            }
        }

        return answer;
    }
}