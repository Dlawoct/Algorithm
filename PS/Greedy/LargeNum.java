import java.util.*;

public class LargeNum {

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();

        int[] arr = new int[n];
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr);
        int first = arr[n-1];
        int second = arr[n-2];

        //제일 큰 수의 사용되는 횟수 -> cnt
        int cnt = (m / k+1) * k;
        cnt += m % (k+1);

        int result = cnt * first + (m - cnt) * second;
    }
}
