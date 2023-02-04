class Solution {
public:
    string convert(string s, int numRows) {
        string ret = "";
        int a = 0; int b = 0; bool c = false;
        if(numRows == 1){
            return s;
        }
        for(int i =0;  i < numRows; i++){
            b = i;
            while(b < s.length() ){
                 if(numRows - 1 == i || i == 0){
                a = (numRows -1) *2 ;
            }else if(!c){
            a = (numRows - i -1) *2 ;
                    c = true ;
                 }else if(c){
                     a = i * 2;
                     c = false;
                 }
                ret += s[b];
                b +=a;
            }
            c = false;
        }
        return ret;
    }
};