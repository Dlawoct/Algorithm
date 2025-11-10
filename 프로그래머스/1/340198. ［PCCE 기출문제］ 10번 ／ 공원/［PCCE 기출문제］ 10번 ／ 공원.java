import java.util.Arrays;

class Solution {
    public int solution(int[] mats, String[][] park) {
        int answer = -1;
        int rows = park.length;
        int cols = park[0].length;
        Arrays.sort(mats);
        
        for(int i = mats.length-1; i >= 0; i--){
            int mat = mats[i];
            
            if (checkPlace(mat, park, rows, cols)){
                answer = mat;
                break;
            }
        }
        
        return answer;
    }
    
    private boolean checkPlace(int mat, String[][] park, int rows, int cols){
        
        for(int i = 0; i <= rows - mat; i++){
            for(int j = 0; j <= cols - mat; j++){
                
                boolean check = true;
                
                for(int k = 0; k < mat; k++){
                    for(int l = 0; l < mat; l++){
                        if(!park[k+i][l+j].equals("-1")){
                            check = false;
                            break;
                        }
                    }
                    if(!check){
                        break;
                    }
                }
                if(check){
                    return true;
                }
            }
        }
        
        return false;
    }
}
// -1이면 돗자리를 펼 수 있는 지 확인
// 제일 큰 돗자리부터 시작해서 NxN 크기가 가능한지 확인
// 안되면 즉시 false하고 다음 -1 찾기
// 계속 반복 후 다음 작은 매트로
// 만약에 매트가 깔리면 즉시 fasle해서 answer 반환