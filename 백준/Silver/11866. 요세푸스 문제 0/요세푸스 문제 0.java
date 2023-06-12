import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.io.IOException;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nk = br.readLine().split(" ");
        int n = Integer.parseInt(nk[0]);
        int k = Integer.parseInt(nk[1]);
        String answer = "<";
        LinkedList<Integer> circle = new LinkedList<>();

        for (int i = 1; i <= n; i++) {
            circle.add(i);
        }
        int size = circle.size();
        int idx = -1;

        while (size > 0) {
            idx = (idx + k) % size;
            if (size == 1) {
                answer = answer + circle.get(idx) + ">";
            } else {
                answer = answer + circle.get(idx) + ", ";
            }
            circle.remove(idx);
            size -= 1;
            idx -= 1;
        }

        System.out.println(answer);
        
    }
}