import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.EmptyStackException;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            char[] arr = br.readLine().toCharArray();
            Stack<Character> stack = new Stack<>();
            boolean wrong = false;
            for (int j = 0; j < arr.length; j++) {
                if (arr[j] == '(') { stack.push(arr[j]); }
                else {
                    try {
                        stack.pop();
                    } catch (EmptyStackException e) {
                        wrong = true;
                        break;
                    }
                    
                }
            }
            if (wrong) {
                bw.write("NO\n");
            } else {
                if (stack.size() == 0) { bw.write("YES\n"); }
                else { bw.write("NO\n"); }
            }

        
        }

        bw.flush();

        br.close();
        bw.close();
    }
}