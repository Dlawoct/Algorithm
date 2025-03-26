import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 빠른 입력을 위한 BufferedReader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 빠른 출력을 위한 BufferedWriter
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] num = new int[n];

        for (int i = 0; i < n; i++) {
            num[i] = Integer.parseInt(br.readLine());
        }

        // 정렬 (Arrays.sort()는 O(N log N))
        Arrays.sort(num);

        for (int i = 0; i < n; i++) {
            bw.write(num[i] + "\n"); // BufferedWriter로 빠른 출력
        }

        // 버퍼 비우고 출력
        bw.flush();
        bw.close();
        br.close();
    }
}