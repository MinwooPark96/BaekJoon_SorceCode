//
//  main.cpp
//  BaekJoon
//
//  Created by Minwoo on 2022/09/23.
//
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
//#include <functional>
#include <map>
//#include <unordered_map>
#include <deque>
#include <list>
//#include <queue>
//using std::cout;
//using std::cin;
#include <math.h>

/*------------------function------------*/
//정답 변수

int num_v;
int num_e;
int curtime=0;
std::map<int,std::vector<int>> children;
std::map<int,std::vector<int>> children_T;

std::map<int,int> finish_time;
std::map<int,int> detect_time;

std::deque<int> finish_stack;
std::map<int,int> stack_point;

std::set<std::set<int>> answer;
std::set<int> island;
std::map<int,int> visit;


void DFS(int parent){
    visit[parent]=1;
    curtime++;
    detect_time[parent]=curtime;
    for (int child : children[parent]){
        if (detect_time[child]==0){
            visit[child]=1;
            DFS(child);
            
        }
    }
    curtime++;
    finish_time[parent]=curtime;
    finish_stack.push_back(curtime);
    stack_point[curtime]=parent;
    
}




void DFS_T(int parent){
    visit[parent]=1;
    auto parent_address=std::find(finish_stack.begin(),finish_stack.end(),finish_time[parent]);
    if (parent_address==finish_stack.end()){
        std::cout<<*parent_address<<'\n';
    }
    else{finish_stack.erase(parent_address);}
    island.insert(parent);
    for (int child : children_T[parent]){
        if (visit[child]==0)
        {DFS_T(child);}
    }
}











/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    /*-----------code-----------------*/

    std::cin>>num_v;
    std::cin>>num_e;
    // children, childrent_T 초기화
    for (int i=1;i<=num_v;i++){
        std::vector<int> bucket;
        children.insert({i,bucket});
        std::vector<int> bucket_T;
        children_T.insert({i,bucket_T});
    }
    
    // finish_time, detect_time 초기화 = 0
    for (int i=1;i<=num_v;i++){
        finish_time[i]=0;
        detect_time[i]=0;
        visit[i]=0;
    }
    
    // children 받아오기 (EDGE)
    for (int i=0;i<num_e;i++){
        int parent;
        int child;
        std::cin>>parent;
        std::cin>>child;
        children[parent].push_back(child);
    }
    
    // 순방향 DFS
    for (int i=1;i<=num_v;i++){
        if (visit[i]==0){
            DFS(i);
            
        }
    }
    
    for (int i=1;i<=num_v;i++){
        visit[i]=0;
    }
    
    // children_T 만들기
    
    for (auto iter=children.begin();iter!=children.end();iter++){
        int i = (*iter).first;
        for (int j : children[i]){
            children_T[j].push_back(i);
        }
    }
    
    
    while (!finish_stack.empty()){
        island.clear();
        
        int finish_time=finish_stack.back();
        int parent=stack_point[finish_time];
        DFS_T(parent);
        
        answer.insert(island);
    }
    std::cout<<answer.size()<<'\n';
    for (auto i : answer){
        for (auto j : i){
            std::cout<<j<<' ';
        }
        std::cout<<"-1\n";
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    /*-----------code-----------------*/

    
    
    return 0;
    
}

/*------------------function------------*/



/*-------------function-----------------*/

