import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Deque;
import java.util.ArrayDeque;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Deque<Integer> deque = new ArrayDeque<>();

        for (int i = 1; i <= n; i++) {
            String cmd = br.readLine();
            int answer = 0;
            switch (cmd) {
                case "pop_front":
                answer = (deque.isEmpty()) ? -1 : deque.poll();
                System.out.println(answer);
                break;

                case "pop_back":
                answer = (deque.isEmpty()) ? -1 : deque.pollLast();
                System.out.println(answer);
                break;

                case "size":
                answer = deque.size();
                System.out.println(answer);
                break;

                case "empty":
                answer = (deque.isEmpty()) ? 1 : 0;
                System.out.println(answer);
                break;

                case "front":
                answer = (deque.isEmpty()) ? -1 : deque.peek();
                System.out.println(answer);
                break;

                case "back":
                answer = (deque.isEmpty()) ? -1 : deque.peekLast();
                System.out.println(answer);
                break;

                default:
                String[] cmds = cmd.split(" ");
                if (cmds[0].equals("push_front")) {
                    deque.addFirst(Integer.parseInt(cmds[1]));
                } else {
                    deque.add(Integer.parseInt(cmds[1]));
                }
                break;
            }
        }
        
    }
}