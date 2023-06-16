import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.math.BigInteger;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> arr = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            arr.add(num);
        }

        Collections.sort(arr);
        for (int j = 0; j < n; j++) {
            bw.write(arr.get(j)+"\n");
        }
        bw.flush();
    }
}