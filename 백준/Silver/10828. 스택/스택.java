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
        Stack<Integer> stack = new Stack<>();

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            int answer = -1; 
            switch (input) {
                case "pop":
                    try {
                        answer = stack.pop();
                    } catch(EmptyStackException e) { }
                    bw.write(answer + "\n");
                    break;

                case "size":
                    answer = stack.size();
                    bw.write(answer + "\n");
                    break;

                case "empty":
                    if (stack.isEmpty()) { answer = 1;} else { answer = 0;}
                    bw.write(answer + "\n");
                    break;

                case "top":
                    try {
                        answer = stack.peek();
                    } catch(EmptyStackException e) {}
                    bw.write(answer + "\n");
                    break;
                
                default:
                    String[] arr = input.split(" ");
                    stack.push(Integer.parseInt(arr[1]));
                    break;
            }
        }

        bw.flush();

        br.close();
        bw.close();
    }
}