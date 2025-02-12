import java.util.Scanner;
import java.util.Arrays;

public class rope {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] k = new int[n];
        for (int i = 0; i < n; i++) {
            k[i] = sc.nextInt();
        }

        Arrays.sort(k);
        int maxWeight = 0;

        for (int i = 0; i < n; i++) {
            int weight = k[i] * (n - i);    //각 로프별로 들 수 있는 최대 중량
            maxWeight = Math.max(maxWeight, weight);    // 현재 최대 중량과 이전 최대 중향을 비교해서 최대 무개로 설정
        }

        System.out.println(maxWeight);
    }
}
