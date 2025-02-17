import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 입력이 있을 때 까지 반복
        while (scanner.hasNext()) {
            String result = "Yes";
            char[] s = scanner.next().toCharArray();
            String t = scanner.next();

            // t에서 비교를 시작할 인덱스
            int start = 0;

            for (int i = 0; i < s.length; i++) {

                while (true) {
                    if (start >= t.length()) {
                        result = "No";
                        break;
                    }
                    if (s[i] == t.charAt(start)) {
                        start++;
                        break;
                    } else {
                        start++;
                    }
                }
            }

            System.out.println(result);
        }
    }
}
