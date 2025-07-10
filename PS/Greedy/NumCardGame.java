import java.util.Scanner;

public class NumCardGame {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int result = 0;

        for(int i = 0; i < n; i++){

            int min = Integer.MAX_VALUE;

            // 해당 행에서 가장 작은 수
            for(int j = 0; j < m; j++){
                int tmp = sc.nextInt();
                min = Math.min(min, tmp);
            }

            // 행에서 가장 작은 수들 중 가장 큰 수
            result = Math.max(result, min);
        }

        System.out.println(result);
    }
}
