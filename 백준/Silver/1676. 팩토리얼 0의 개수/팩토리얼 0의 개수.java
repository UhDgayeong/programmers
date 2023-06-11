import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        BigInteger factorial = BigInteger.ONE;
        int answer = 0;

        for (int i = 2; i <= n; i++) {
            factorial = factorial.multiply(BigInteger.valueOf(i));
        }

        char[] arr = factorial.toString().toCharArray();
        for (int j = arr.length - 1; j >= 0 ; j--) {
            if (Character.compare(arr[j], '0') == 0) {
                answer += 1;
            } else {
                break;
            }
        }

        System.out.println(answer);
        
    }
}