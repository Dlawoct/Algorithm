class Solution {
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        int n = board.length;
        String color = board[h][w];
        int[][] direction = {{1,0},{0,1},{-1,0},{0,-1}};
        
        for (int i = 0; i < 4; i++){ 
            int dh = h + direction[i][0];
            int dw = w + direction[i][1];
        
            if(dh <= -1 || dw <= -1 || dh >= n || dw >= n){
                continue;
            }
            if (board[dh][dw].equals(color)){
                answer++;
            }
            
        }
        
        return answer;
    }
}