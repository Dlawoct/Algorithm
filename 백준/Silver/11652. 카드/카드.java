import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        // hashMap 생성 후 매핑
        Map<Long, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            long m = Long.parseLong(br.readLine());
            map.put(m, map.getOrDefault(m, 0) + 1);
        }

        // 최대 빈도수와 최빈값
        int maxNum = 0;
        long num = 0;

        //map에서 빈도수 체크
        for (long i : map.keySet()) {
            //기존 maxNum보다 크면 교체
            if (map.get(i) > maxNum) {
                maxNum = map.get(i);
                num = i;
                // 같은 경우 작은 숫자가 최대 빈도 num
            } else if (map.get(i) == maxNum) {
                num = Math.min(i, num);
            }
        }
        System.out.println(num);
    }

}
