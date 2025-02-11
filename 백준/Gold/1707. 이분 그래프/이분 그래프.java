/*
import java.util.Scanner;

public class BipartiteGraph {
    static int[][] graph;
    static int[] visit; // 0: 미방문, 1: 1번 그룹, 2: 2번 그룹
    static int K, V, E;


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        K = sc.nextInt();

        while (K-- > 0) {
            V = sc.nextInt();
            E = sc.nextInt();

            graph = new int[V + 1][V + 1];
            visit = new int[V + 1];

            for (int i = 0; i < E; i++) {
                int a = sc.nextInt();
                int b = sc.nextInt();
                graph[a][b] = 1;
                graph[b][a] = 1;
            }

            boolean isBiparite = true;
            for (int i = 1; i <= V; i++) {
                if (visit[i] == 0) {    // 방문했는 지 확인
                    if (!(dfs(i, 1))) { // 방문 안했으면 1번 그룹으로 시작
                        isBiparite = false;
                        break;
                    }
                }
            }

            if (isBiparite) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }

    public static boolean dfs(int node, int c) {
        visit[node] = c;

        for (int next = 1; next <= V; next++) {
            if (graph[node][next] == 1) { // 간선이 있는 경우
                if (visit[next] == 0) { // 방문하지 않은 경우
                    if (!dfs(next, 3 - c)) return false; // 다른 그룹으로 표시
                } else if (visit[next] == c) { // 같은 색이 나오면 false
                    return false;
                }
            }
        }
        return true;

    }
}
*/

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static ArrayList<Integer>[] graph; // 인접 리스트
    static int[] visit; // 0: 미방문, 1: 그룹1, 2: 그룹2
    static int K, V, E;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        K = sc.nextInt();

        while (K-- > 0) {
            V = sc.nextInt();
            E = sc.nextInt();

            graph = new ArrayList[V + 1]; // 리스트 초기화
            visit = new int[V + 1];

            for (int i = 1; i <= V; i++) {
                graph[i] = new ArrayList<>();
            }

            for (int i = 0; i < E; i++) {
                int a = sc.nextInt();
                int b = sc.nextInt();
                graph[a].add(b);
                graph[b].add(a);
            }

            boolean isBiparite = true;
            for (int i = 1; i <= V; i++) {
                if (visit[i] == 0) { // 방문하지 않은 경우
                    if (!dfs(i, 1)) { // 그룹1로 시작
                        isBiparite = false;
                        break;
                    }
                }
            }

            if (isBiparite) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }

    public static boolean dfs(int node, int c) {
        visit[node] = c;

        for (int next : graph[node]) { // 연결된 모든 정점 탐색
            if (visit[next] == 0) { // 방문하지 않은 경우
                if (!dfs(next, 3 - c)) return false; // 다른 그룹으로 지정
            } else if (visit[next] == c) { // 같은 색이면 실패
                return false;
            }
        }
        return true;
    }
}
