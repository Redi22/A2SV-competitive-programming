#include <string.h>

class Solution {
public:
    int romanToInt(string s) {
        int n = 0;
        int converted = 0;
        while(n < s.length()){
            if(s.compare(n , 1 , "M") == 0){
                converted = converted + 1000;
                n++;
            }else if(s.compare(n , 1 , "D") == 0){
                converted = converted + 500;
                n++;
            }else if(s.compare(n , 1 , "L") == 0 ){
                converted = converted + 50;
                n++;
            }else if(s.compare(n , 1 , "V") == 0 ){
                converted = converted + 5;
                n++;
            }else if (s.compare(n , 1 , "C") == 0 ){
                if( s.compare(n+1 , 1 , "M") == 0 )
                {
                    converted = converted + 900;
                    n+=2;
                }else if(s.compare(n+1 , 1 , "D") == 0 ){
                    converted = converted + 400;
                    n+=2;
                }else{
                    converted = converted + 100;
                    n++;
                }
            }else if (s.compare(n , 1 , "I") == 0  ){
                if(s.compare(n+1 , 1 , "V") == 0 )
                {
                    converted = converted + 4;
                    n+=2;
                }else if(s.compare(n+1 , 1 , "X") == 0){
                    converted = converted + 9;
                    n+=2;
                }else{
                    converted = converted + 1;
                    n++;
                }
            }else if (s.compare(n , 1 , "X") == 0 ){
                if(s.compare(n+1, 1 , "L") == 0 )
                {
                    converted = converted + 40;
                    n+=2;
                }else if(s.compare(n+1 , 1 , "C") == 0 ){                    
                    converted = converted + 90;
                    n+=2;
                }else{
                    converted = converted + 10;
                    n++;
                }
            }
        }
        return converted;
    }
};