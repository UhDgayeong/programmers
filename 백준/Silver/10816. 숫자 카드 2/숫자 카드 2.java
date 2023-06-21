import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        HashMap<String, Integer> hm = new HashMap<>();
        StringBuilder answer = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        String[] cards = br.readLine().split(" ");

        for (int i = 0; i < n; i++) {
            if (hm.containsKey(cards[i])) {
                hm.put(cards[i], hm.get(cards[i]) + 1);
            } else {
                hm.put(cards[i], 1);
            }
        }

        int m = Integer.parseInt(br.readLine());
        String[] arr = br.readLine().split(" ");

        for (int i = 0; i < m; i++) {
            int j = 0;
            if (hm.containsKey(arr[i])) {
                j = hm.get(arr[i]);
            }
            answer.append(j).append(" ");
        }


        bw.flush();
        bw.write(answer.toString().trim());

        br.close();
        bw.close();
    }
}