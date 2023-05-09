import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        char[] str = a.toCharArray(); 
        int idx = 0;
        
        for (char c : str) {
            if (Character.isUpperCase(c)) {
                str[idx] = Character.toLowerCase(c);
            }
            else {
                str[idx] = Character.toUpperCase(c);
            }
            idx += 1;
        }
        
        System.out.print(str);
    }
}