import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Main{

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Map<Integer, Integer> map = new HashMap<>();

        int n = Integer.parseInt(br.readLine());
        int[] num = new int[n];
        int[] sorted = new int[n];

        String[] input = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            num[i] = Integer.parseInt(input[i]);
            sorted[i] = num[i];
        }

        Arrays.sort(sorted);

        int rank = 0;
        for (int value : sorted) {
            if(!map.containsKey(value)){
                map.put(value,rank);
                rank++;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int value : num) {
            sb.append(map.get(value)).append(" ");
        }

        System.out.println(sb);

    }
}

