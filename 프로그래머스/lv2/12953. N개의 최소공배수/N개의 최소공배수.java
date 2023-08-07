import java.util.ArrayList;

class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        int product = 1;
        ArrayList<Integer> list = new ArrayList<Integer>();
        
        for (int a : arr) {
            list.add(a);
            product *= a;
        }
        
        while (list.size() > 1) {
            int gcd_val = gcd(list.get(0), list.get(1));
            int lcm_val = list.get(0) * list.get(1) / gcd_val;
            list.remove(0);
            list.remove(0);
            list.add(0, lcm_val);
        } 
        
        answer = list.get(0);
        return answer;
    }
    
    // 최대공약수 구하는 메소드
    public int gcd(int a, int b) {
        if (a % b == 0) {
            return b;
        } else {
            return gcd(b, a % b);
        }
    }
}