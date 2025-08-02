import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class UpDownLeftRight {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] plans = br.readLine().split(" ");
        int x = 1, y = 1;

        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        String[] direction = {"U", "D", "L", "R"};

        for( String plan : plans){
            int nx = 0, ny = 0;
            for( int i = 0; i < direction.length; i++ ){
                if (plan.equals(direction[i])){
                    nx = x + dx[i];
                    ny = y + dy[i];
                }
            }

            if(nx < 1 || ny < 1 || nx > n || ny > n){
                continue;
            }

            x = nx;
            y = ny;
        }
        System.out.println(x + " " + y);
    }
}
