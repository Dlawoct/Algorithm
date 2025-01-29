import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[][] rooms = new int[n][2];

        // 회의실 배정
        for (int i = 0; i < n; i++) {
            rooms[i][0] = scanner.nextInt();
            rooms[i][1] = scanner.nextInt();
        }

        // 오름 차순으로 정렬 (람다 함수)
        Arrays.sort(rooms, (a, b) -> {
            if (a[1] == b[1]) {
                return a[0] - b[0];
            }
            return a[1] - b[1];
        });

        int count = 0;
        int lastEndtime = 0;

        // 이전 회의의 종료 시간보다 이상이면 count +1, 종료 시간 업데이트
        for (int[] room : rooms) {
            if (room[0] >= lastEndtime) {
                count++;
                lastEndtime = room[1];
            }
        }

        System.out.println(count);
    }
}
