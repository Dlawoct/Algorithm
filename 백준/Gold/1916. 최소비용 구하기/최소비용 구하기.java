import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Main {
    static int N, M; // 도시 수와 버스 수
    static ArrayList<ArrayList<Node>> graph; // 그래프
    static int[] dist; // 최소 비용 저장 배열

    static class Node implements Comparable<Node> {
        int city, cost;

        public Node(int city, int cost) {
            this.city = city;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node other) {
            return this.cost - other.cost; // 비용이 작은 순으로 정렬
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 도시와 버스 입력
        N = scanner.nextInt();
        M = scanner.nextInt();

        // 그래프 초기화
        graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>()); // 각 도시별 연결 리스트 생성
        }

        // 그래프 입력받기
        for (int i = 0; i < M; i++) {
            int from = scanner.nextInt();
            int to = scanner.nextInt();
            int cost = scanner.nextInt();
            graph.get(from).add(new Node(to, cost)); // 그래프에 추가
        }

        // 시작점과 도착점 입력
        int start = scanner.nextInt();
        int end = scanner.nextInt();

        // 최단 경로 계산
        int result = dijkstra(start, end);

        // 결과 출력
        System.out.println(result);
    }

    public static int dijkstra(int start, int end) {
        // 최소 비용 배열 초기화
        dist = new int[N + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0; // 시작 도시는 비용 0

        // 우선순위 큐로 다익스트라 실행
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node current = pq.poll();
            int currentCity = current.city;
            int currentCost = current.cost;

            // 이미 처리된 비용이면 넘어감
            if (currentCost > dist[currentCity]) continue;

            // 현재 도시에서 이동 가능한 도시 탐색
            for (Node neighbor : graph.get(currentCity)) {
                int nextCity = neighbor.city;
                int nextCost = currentCost + neighbor.cost;

                // 더 적은 비용으로 갈 수 있으면 갱신
                if (nextCost < dist[nextCity]) {
                    dist[nextCity] = nextCost;
                    pq.add(new Node(nextCity, nextCost));
                }
            }
        }

        return dist[end]; // 도착점까지의 최소 비용 반환
    }
}