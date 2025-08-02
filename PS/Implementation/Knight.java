import java.util.Scanner;

public class Knight {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String knight = sc.nextLine();
        int x = knight.charAt(0) - 'a' + 1;
        int y = knight.charAt(1) - '0';

        int[] dx = {-2, -2, 2, 2, -1, 1, -1, 1};
        int[] dy = {-1, 1, -1, 1, -2, -2, 2, 2};

        int result = 0;

        for(int i = 0; i < 8; i++){

            int nextX = x + dx[i];
            int nextY = y + dy[i];

            if (nextX >= 1 && nextX <= 8 && nextY >= 1 && nextY <= 8) {
                result++;
            }
        }

        System.out.println(result);

    }
}
