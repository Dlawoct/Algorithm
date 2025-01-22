import java.util.Scanner;

public class RGB {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] rgb = new int[n][3];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 3; j++){
                rgb[i][j] = sc.nextInt();
            }
        }
        int[][] dp = new int[n][3];

        // 첫번째 집 초기화
        dp[0][0] = rgb[0][0];
        dp[0][1] = rgb[0][1];
        dp[0][2] = rgb[0][2];

        // dp를 이용해서 색이 겹치지않는 최소값 구하기
        for (int i = 1; i < n; i++) {
            dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2]) + rgb[i][0];
            dp[i][1] = Math.min(dp[i-1][0], dp[i-1][2]) + rgb[i][1];
            dp[i][2] = Math.min(dp[i-1][0], dp[i-1][1]) + rgb[i][2];
        }

        int result = Math.min(Math.min(dp[n-1][0], dp[n-1][1]), dp[n-1][2]);
        System.out.println(result);

    }
}
