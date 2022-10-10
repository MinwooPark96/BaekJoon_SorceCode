//
//  main.cpp
//  BaekJoon
//
//  Created by Minwoo on 2022/09/23.
//
#include <iostream>
#include <vector>
//#include <algorithm>
#include <set>
//#include <functional>
//#include <map>
//#include <unordered_map>
#include <deque>
//#include <list>
//#include  <queue>
//using std::cout;
//using std::cin;

// 백준 14500 번


/*------------------function------------*/
//정답 변수

std::vector<int> neighboor(int n){
    std::vector<int> result(3);
    result[0]=n-1;
    result[1]=n+1;
    result[2]=n*2;
    return result;
    
}


/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    /*-----------code-----------------*/
    std::deque<int> my_deq;
    
    int n,k; std::cin>>n>>k;
    
    if (k<=n){
        std::cout<<n-k;
        exit(0);
    }
    
    
    int visit[200002];
    
    visit[n]=1;
    my_deq.push_back(n);
    
    while (!my_deq.empty()){
        int cur_n=my_deq.front();
        if (cur_n==k){
            std::cout<<visit[cur_n]-1;
            break;
        }
        my_deq.pop_front();
        for (int child: neighboor(cur_n)){
                if(child<=100000 && child >=0 && visit[child]==0){
                    visit[child]=visit[cur_n]+1;
                    my_deq.push_back(child);
                }
            }
        
        
        
        
    }
    
    

    
    /*-----------code-----------------*/

    
    return 0;
}

/*------------------function------------*/



















/*-------------function-----------------*/

