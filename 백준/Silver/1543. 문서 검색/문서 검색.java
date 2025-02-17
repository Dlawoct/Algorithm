import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // 문자열 받기
        String doc = scanner.nextLine();
        String str = scanner.nextLine();
        
        // 문자열 길이 미리 저장
        int docLen = doc.length();
        int strLen = str.length();
        
        // str에 해당하는 doc의 문자열 다 제거
        doc = doc.replace(str, "");
        // str만 적혀있는 doc 문자열의 갯수 / str 길이
        System.out.println((docLen - doc.length()) / strLen);
    }
}
