import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            br.readLine(); // 빈 줄로 케이스 분류
            st = new StringTokenizer(br.readLine()); // 각 케이스의 r, c값
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            char[][] arr = new char[r][c];
            int candy = 0;

            for (int j = 0; j < r; j++) {
                String line = br.readLine();
                for (int k = 0; k < c; k++) {
                    arr[j][k] = line.charAt(k);
                }
            }

            for (int j = 0; j < r; j++) {
                for (int k = 0; k < c; k++) {
                    if (k < c-2 && arr[j][k] == '>' && arr[j][k+1] == 'o' && arr[j][k+2] == '<') {
                        candy += 1;
                    } else if (j < r-2 && arr[j][k] == 'v' && arr[j+1][k] == 'o' && arr[j+2][k] == '^') {
                        candy += 1;
                    }
                }
            }

            System.out.println(candy);
        }
    }
}