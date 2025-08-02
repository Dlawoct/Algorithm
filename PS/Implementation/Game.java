import java.util.Scanner;

public class Game {

    public static int z;

    public static void turn_left() {
        z -= 1;
        if (z == -1) z = 3;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int [][] board = new int[N][M];

        int x = sc.nextInt();
        int y = sc.nextInt();
        z = sc.nextInt();
        int [][] d = new int[N][M];
        d[x][y] = 1;

        int [] dx = {0, 1, 0, -1};
        int [] dy = {-1, 0, 1, 0};

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                board[i][j] = sc.nextInt();
            }
        }

        int result = 1;
        int turn = 0;
        while (true) {
            turn_left();
            int nx = x + dx[z];
            int ny = y + dy[z];

            if (d[nx][ny] == 0 && board[nx][ny] == 0) {
                d[nx][ny] = 1;
                x = nx;
                y = ny;
                result++;
                turn = 0;
                continue;
            } else {
                turn++;
            }
            if(turn == 4){
                nx = x - dx[z];
                ny = y - dy[z];
                if(board[nx][ny] == 0){
                    x = nx;
                    y = ny;
                } else break;
                turn = 0;
            }
        }

        System.out.println(result);
    }
}
