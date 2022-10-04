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
#include <map>
//#include <unordered_map>
#include <deque>
#include <list>

//using std::cout;
//using std::cin;

// 백준 16234 번
//2 20 50
//50 30
//20 40
//


/*------------------function------------*/

int dx[4]={-1,0,1,0};
int dy[4]={0,1,0,-1};
int answer=0;
int stop;
//한점에 대한 DFT
void DFT(std::vector<std::vector<int>>&visit,std::vector<std::vector<int>>& matrix,int l,int r,std::pair<int,int> start){
    
    int n = (int)visit.size();
    int count=1;
    std::deque<std::pair<int,int>> my_deq;
    std::map<std::pair<int,int>,int> island; //연결된 점,값
    
    my_deq.push_back(start);
    visit[start.first][start.second]=1;
    
    while (my_deq.empty()==0){
        std::pair<int,int> curpoint=my_deq.front(); my_deq.pop_front();
        island.insert({{curpoint.first,curpoint.second},matrix[curpoint.first][curpoint.second]});//섬에 추가
        
        for (int i=0;i<4;i++){
            int child_x=curpoint.first+dx[i];
            int child_y=curpoint.second+dy[i];
            if (0<=child_x && child_x<n && 0<=child_y && child_y<n){
                int difference=std::abs(matrix[curpoint.first][curpoint.second]-matrix[child_x][child_y]);
                if(visit[child_x][child_y]==0 && l<=difference
                   && difference<=r){
                    visit[child_x][child_y]=1; //visit 에 추가
                    my_deq.push_back({child_x,child_y});
                    count++;
                    
                }
            }
        }
    }

    if(count>1){stop=0;} //섬이 비어있지않으면 stop=0
    else{return;}
    //--- 여기서 부터 평균을 계산해서 수정하는 구간 -- if에 걸리는 구간
    int avg=0;
    for (std::pair<std::pair<int,int>,int> i: island){
        avg+=i.second;
    }
    avg/=island.size();
    
    for (std::pair<std::pair<int,int>,int> i: island){
        int x=i.first.first;
        
        int y=i.first.second;
        matrix[x][y]=avg;
    }

}//함수종료


/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    /*-----------code-----------------*/
    
    int n;std::cin>>n;
    int l;std::cin>>l;
    int r;std::cin>>r;
    
    std::vector<std::vector<int>> matrix(n,std::vector<int>(n,0));
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            std::cin>>matrix[i][j];
        }
    }
    
    while (!stop){
        stop=1;
        std::vector<std::vector<int>> visit(n,std::vector<int>(n,0));
        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                if(visit[i][j]==0){
                    DFT(visit, matrix, l, r, {i,j});}
            }
            
        }
        answer+=1;
    }
    
    std::cout<<answer-1;
    /*-----------code-----------------*/
    return 0;
}

