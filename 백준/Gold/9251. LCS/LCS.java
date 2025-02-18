import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        char[] str1 = scanner.next().toCharArray();
        char[] str2 = scanner.next().toCharArray();

        int str1_length = str1.length;
        int str2_length = str2.length;

        // 1부터 시작하기에 +1
        int[][] dp = new int[str1_length + 1][str2_length + 1];

        for (int i = 1; i <= str1_length; i++) {
            for (int j = 1; j <= str2_length; j++) {

                // i-1 과 j-1 번째 문자가 같다면
                if (str1[i - 1] == str2[j - 1]) {
                    //
                    dp [i][j] = dp[i-1][j-1] + 1;
                }

                // 같지 않다면 이전 행이나 열 중 큰 값으로 갱신
                else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        System.out.println(dp[str1_length][str2_length]);
    }
}
