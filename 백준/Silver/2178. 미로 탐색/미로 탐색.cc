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
//#include <functional>
//#include <map>
//#include <unordered_map>
#include <deque>
//#include <list>
//#include <queue>
//using std::cout;
//using std::cin;

// 백준 2178 번


/*------------------function------------*/
//정답 변수

int answer=0;
int dx[4]={-1,0,1,0};
int dy[4]={0,1,0,-1};

/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    /*-----------code-----------------*/
    
    int n,m;std::cin>>n>>m;
    std::vector<std::vector<int>> matrix(n,std::vector<int>(m,0));
    std::vector<std::vector<int>> visit(n,std::vector<int>(m,0));
    
    for (int i=0;i<n;i++){
        std::string row;
        std::cin>>row;
        for (int j=0;j<m;j++){
            matrix[i][j]=row[j]-'0';
        }
        
    }
    std::copy(matrix.begin(),matrix.end(),visit.begin());
    std::pair<int, int> start={0,0};
    std::deque<std::pair<int, int>> my_deq;
    
    
    my_deq.push_back(start);
    
    while (!my_deq.empty()){
        std::pair cur=my_deq.front();my_deq.pop_front();
        int cur_x=cur.first;
        int cur_y=cur.second;
        for (int i=0;i<4;i++){
            int child_x=cur_x+dx[i];
            int child_y=cur_y+dy[i];
            if (0<=child_x && child_x<n && 0<=child_y && child_y<m && visit[child_x][child_y]==1&&child_x+child_y!=0){
                visit[child_x][child_y]=visit[cur_x][cur_y]+1;
                my_deq.push_back({child_x,child_y});
            }
            
            
        }
        
        
        
    }
    answer=visit[n-1][m-1];
    std::cout<<answer;
    
    
    
    
    
    
    /*-----------code-----------------*/

    
    return 0;
}

/*------------------function------------*/





