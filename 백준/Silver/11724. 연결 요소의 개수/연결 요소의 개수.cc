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
#include <map>
//#include <unordered_map>
//include <deque>
//#include <list>
#include <queue>
//using std::cout;
//using std::cin;

// 백준 14500 번


/*------------------function------------*/
//정답 변수

int answer=0;

/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::deque<int> my_deq;
    
    /*-----------code-----------------*/
    
    int n,m;std::cin>>n>>m;
    std::map<int,std::vector<int>> edge;
    for (int i=0;i<m;i++){
        int x,y; std::cin>>x>>y;
        edge[x].push_back(y);
        edge[y].push_back(x);
        
    }
    
    int visit[n];
    for (int i=0;i<n;i++){
        visit[i+1]=0;
    }

    for (int vertex=1;vertex<=n;vertex++){
        if (visit[vertex]==0){
            answer+=1;
            my_deq.push_back(vertex);
            visit[vertex]=1;
            
            while(!my_deq.empty()){
                int cur_v=my_deq.front();
                my_deq.pop_front();
                for (auto child:edge[cur_v]){
                    if(visit[child]==0){
                        visit[child]=1;
                        my_deq.push_back(child);
                    }
                }
                
            }
            
            
        }
        
        
    }
    
    std::cout<<answer;
    
    
    
    
    
    
    /*-----------code-----------------*/

    
    return 0;
}

/*------------------function------------*/



















/*-------------function-----------------*/

