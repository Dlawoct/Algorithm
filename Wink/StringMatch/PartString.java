import java.util.Scanner;

public class PartString {

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
                    // 비교할 문자열이 더 없을 때
                    if (start >= t.length()) {
                        result = "No";
                        break;
                    }
                    // 두 문자가 일치하면 start 증가, 다음 문자열 비교
                    if (s[i] == t.charAt(start)) {
                        start++;
                        break;
                    }
                    // 일치하지 않으면 start만 증가 시켜 계속 비교
                    else {
                        start++;
                    }
                }
            }
            System.out.println(result);
        }
    }
}
