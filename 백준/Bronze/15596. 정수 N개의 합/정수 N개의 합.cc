#include <vector>

long long sum(std::vector<int> &a){
    long long answer=0;
    for (int i:a){
        answer+=i;
    }
    
    return answer;
    
}


