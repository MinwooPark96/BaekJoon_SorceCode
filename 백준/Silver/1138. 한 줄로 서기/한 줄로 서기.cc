//
//  main.cpp
//  BaekJoon
//
//  Created by Minwoo on 2022/09/23.
//
#include <iostream>
#include <vector>
//#include <algorithm>
//#include <set>
#include <map>
//#include <unordered_map>
//#include <deque>


//using std::cout;
//using std::cin;


/*------------------function------------*/

class mine{
public:
    
};



/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    /*-----------code-----------------*/
    
    int N;std::cin>>N;
    std::map<int,int> answer_map;
    std::vector<int> result(N,-1);
    
    for (int i=1;i<=N;i++){
        int left_num;std::cin>>left_num;
        answer_map.insert({i,left_num});
    }
    
    for (int i=1;i<=N;i++){
        int jump=answer_map.at(i);
        std::vector<int>::iterator iter=result.begin();
        while (jump>0){
            if (*iter==-1) {jump-=1;iter+=1;}
            else {iter+=1;}
        }
        while (1){
            if(*iter==-1) {*iter=i; break;}
            else {iter+=1;}
        }
    }
    
    for (int i : result){
    std::cout<<i<<" ";
    }
    
    /*-----------code-----------------*/
    return 0;
}

