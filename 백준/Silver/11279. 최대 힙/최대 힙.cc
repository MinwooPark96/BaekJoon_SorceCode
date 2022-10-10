//
//  main.cpp
//  BaekJoon
//
//  Created by Minwoo on 2022/09/23.
//
#include <iostream>
#include <vector>
#include <algorithm>
//#include <set>
#include <functional>
#include <map>
//#include <unordered_map>
#include <deque>
#include <list>
#include  <queue>
//using std::cout;
//using std::cin;

// 백준 14500 번


/*------------------function------------*/
//정답 변수


/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    /*-----------code-----------------*/
    
    std::priority_queue<int,std::vector<int>,std::less<int>> pq;
    int n;std::cin>>n;
    
    for (int i=0;i<n;i++){
        int _operator;
        std::cin>>_operator;
        if (_operator==0){
            if(pq.empty()){std::cout<<0<<"\n";}
            else {std::cout<<pq.top()<<"\n";pq.pop();}
        }
        else{
            pq.push(_operator);
        }
    }
    
    
    
    
    
    
    
    /*-----------code-----------------*/

    
    return 0;
}

/*------------------function------------*/



















/*-------------function-----------------*/
