import java.util.*;

class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        int[][] answer = {};
        String[] names = {"code", "date", "maximum", "remain"};
        
        ArrayList<int[]> filter_data = new ArrayList<int[]>();
        
        for(int i = 0; i < data.length; i++){
            if(ext.equals("code")){
                if(data[i][0] < val_ext){
                    filter_data.add(data[i]);
                }
            }
            else if(ext.equals("date")){
                if(data[i][1] < val_ext){
                    filter_data.add(data[i]);
                }
            }
            else if(ext.equals("maximum")){
                if(data[i][2] < val_ext){
                    filter_data.add(data[i]);
                }
            }
            else{
                if(data[i][3] < val_ext){
                    filter_data.add(data[i]);
                }
            } 
        }
        
    
        if(sort_by.equals("code")){
            filter_data.sort((a, b) -> a[0] - b[0]);
        }
        else if(sort_by.equals("date")){
            filter_data.sort((a, b) -> a[1] - b[1]);
        }
        else if(sort_by.equals("maximum")){
            filter_data.sort((a, b) -> a[2] - b[2]);   
        }
        else{
            filter_data.sort((a, b) -> a[3] - b[3]);    
        } 
        
        return filter_data.toArray(new int[filter_data.size()][]);
    }
}

// ext, sort_by -> code, date, maximum, remain
