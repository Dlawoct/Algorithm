import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] dp = new int[n+1];    //n만큼 배열 만들기
        dp[1] = 0;  //1은 계산할 것이 없으므로 0

        for (int i = 2; i <= n; i++) {

            dp[i] = dp[i-1] + 1;    // 기본적으로 1뺀다 생각하고 이전 값에 더하기 1

            if (i % 2 == 0) {   // 2으로 나눠지면 1뺀 것과 2로 나눈것 중 최소값 선택
                dp[i] = Math.min(dp[i], dp[i / 2] + 1);
            }

            if (i % 3 == 0) {   // 3으로 나눠지면 1뺀 것과 3으로 나눈것 중 최소값 선택
                dp[i] = Math.min(dp[i], dp[i / 3] + 1);
            }
        }

        System.out.println(dp[n]);

    }
}