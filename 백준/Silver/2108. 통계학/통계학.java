import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Collections;

public class Main {
    
    public static int average(HashMap<Integer, Integer> hm) {
        int sum = 0;
        float length = 0;
        for (int key: hm.keySet()) {
            sum += key * hm.get(key);
            length += hm.get(key);
        }
        float avg = sum / length;

        return Math.round(avg);
    }

    public static int median(ArrayList<Integer> arr) {
        return arr.get(arr.size() / 2);
    }

    public static int mode(HashMap<Integer, Integer> hm) {
        ArrayList<Integer> mostCommonKeys = new ArrayList<>();
        for (int key: hm.keySet()) {
            if (mostCommonKeys.size() == 0) {
                mostCommonKeys.add(key);
            } else {
                if (hm.get(key) >= hm.get(mostCommonKeys.get(0))) {
                    if (hm.get(key) > hm.get(mostCommonKeys.get(0))) {
                        mostCommonKeys.clear();
                    }
                    mostCommonKeys.add(key);
                } 
            }
        }

        if (mostCommonKeys.size() >= 2) {
            Collections.sort(mostCommonKeys);
            return mostCommonKeys.get(1);
        } else {
            return mostCommonKeys.get(0);
        }

    }

    public static int range(ArrayList<Integer> arr) {
        int answer = 0;
        if (arr.size() != 0) {
            answer = arr.get(arr.size() - 1) - arr.get(0);
            if (answer < 0) {
                answer = answer * (-1);
            }
        }
        return answer;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        HashMap<Integer, Integer> hm = new HashMap<>();
        ArrayList<Integer> arr = new ArrayList<>();
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            if (hm.containsKey(num)) {
                int count = hm.get(num);
                hm.put(num, count + 1);
            } else {
                hm.put(num, 1);
            }
            arr.add(num);
        }
        Collections.sort(arr);

        bw.write(average(hm) + "\n");
        bw.write(median(arr) + "\n");
        bw.write(mode(hm) + "\n");
        bw.write(range(arr) + "\n");

        bw.flush();

        br.close();
        bw.close();
    }
}