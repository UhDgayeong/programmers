import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.lang.Math;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while (true) {
            String[] arr = br.readLine().split(" ");
            int max_idx = 0;

            if (arr[0].equals("0")) {
                break;
            }
            ArrayList<Double> t_case = new ArrayList<>();
            for (int i = 0; i < 3; i++) {
                t_case.add(Double.parseDouble(arr[i]));
            }

            for (int i = 1; i < 3; i++) {
                if (t_case.get(i) > t_case.get(max_idx)) {
                    max_idx = i;
                }
            }

            Double max = t_case.get(max_idx);
            t_case.remove(max_idx);

            if (Math.pow(t_case.get(0), 2) + Math.pow(t_case.get(1), 2) == Math.pow(max, 2)) {
                bw.write("right" + "\n");
            } else {
                bw.write("wrong" + "\n");
            }
        }

        bw.flush();
    }
}