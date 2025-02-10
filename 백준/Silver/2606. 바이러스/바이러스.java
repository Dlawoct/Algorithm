import java.util.Scanner;

public class Main {
    // 모든 클래스에서 접근 가능하도록 선언
    static int map[][];
    static boolean visit[];
    static int n, pair, v;
    static int count = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        pair = sc.nextInt();

        map = new int[n+1][n+1];    // 각 컴퓨터의 탐색 경로를 저장할 배열
        visit = new boolean[n+1]; // 탐색 여부

        for (int i = 0; i < pair; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            map[a][b] = map[b][a] = 1;
        }

        System.out.println(dfs(1));

    }

    // 깊이 우선 탐색
    public static int dfs(int i) {
        visit[i] = true;

        for (int j = 1; j <= n; j++) {
            // 관계가 있고 방문을 안했으면
            if (map[i][j] == 1 && visit[j] == false) {
                count++;
                dfs(j);
            }
        }
        return count;
    }
}