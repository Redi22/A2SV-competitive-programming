class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> str;
        for(int i = 1; i <= n ; i++ ){
            if(i % 3 == 0){
                if(i % 5 == 0){
                    str.push_back("FizzBuzz") ;
                }else{
                    str.push_back("Fizz");
                }
            }else if(i % 5 == 0) {
                str.push_back("Buzz");
            }else{
                str.push_back(to_string(i));
                
            }
        }
        return str;
    }
};