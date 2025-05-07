import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        // 식을 리스트에 넣기
        List<String> list = new ArrayList<>();
        StringBuilder num = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (c == '+' || c == '-') {
                list.add(num.toString());
                list.add(String.valueOf(c));
                num.setLength(0);
            } else {
                num.append(c);
            }
        }
        list.add(num.toString());

        // "-"가 나오는 idx 찾기
        int idx = 0;
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i).equals("-")) {
                idx = i;
                break;
            }
        }

        // "-"가 없을 때
        if (idx == 0) {
            int sum = Integer.parseInt(list.get(0));
            for (int i = 2; i < list.size(); i += 2) {
                sum += Integer.parseInt(list.get(i));
            }
            System.out.println(sum);
        // "-"가 있을 때
        } else {
            int firstSum = Integer.parseInt(list.get(0));
            for (int i = 2; i < idx; i += 2) {
                firstSum += Integer.parseInt(list.get(i));
            }

            int secondSum = 0;
            for (int i = idx + 1; i < list.size(); i += 2) {
                secondSum += Integer.parseInt(list.get(i));
            }

            int result = firstSum - secondSum;
            System.out.println(result);
        }


    }
}
