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

// 백준 14502 번


/*------------------function------------*/

static int n,m;
static int dx[4]={-1,0,1,0};
static int dy[4]={0,-1,0,1};
static int Answer=0;
static int result=0;

void DFS(std::vector<std::vector<int>>&,int,int);
void wall(std::vector<std::vector<int>>&,int);
/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    /*-----------code-----------------*/
    
    std::cin>>n>>m;
    std::vector<std::vector<int>> matrix(n,std::vector<int>(m,0));
    std::vector<std::vector<int>> visit;
    
    
    for (int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            std::cin>>matrix[i][j];
            
        }
    }
    //visit 에 matrix 를 복사
    visit.assign(n,std::vector<int>(m));
    std::copy(matrix.begin(), matrix.end(),visit.begin());
    
    
//    wall(visit,0);
    
    wall(visit,0);
    std::cout<<Answer;
    
    
    
    
    
    
    
    
    /*-----------code-----------------*/
    return 0;
}

/*------------------function------------*/



//벽 3개가 새워져 있다는 가정하에 dfs 를 통해서 바이러스를 퍼트린 후 0의 개수를 새어야 한다.
void DFS(std::vector<std::vector<int>>& visit,int x,int y){ //x,y 가 바이러스 점(2) 이라고 가정 , 바이러스는 1이 아닌 점은 모두 들어간다.
    std::deque<std::pair<int,int>> my_deq;
    std::pair<int,int> start = {x,y};
    visit[x][y]=3; //방문한 바이러스는 3으로 표시하자.
    my_deq.push_back(start);//덱에 시작점 넣고
    //시작점을 포함해 시작점과 연계된 안전공간과 바이러스공간은 모두 3으로 표시될것 -> 따라서 바이러스지점(2)만 인풋으로 받으면됨.
    
    while (my_deq.size()){ //덱이 비어있지 않는 동안에
        std::pair curpair=my_deq.front();
        my_deq.pop_front();
        int cur_x=curpair.first;
        int cur_y=curpair.second;
        for (int i=0;i<4;i++){
            int child_x=cur_x+dx[i];
            int child_y=cur_y+dy[i];
            if (0<=child_x && child_x<n && 0<=child_y && child_y<m){
                if (visit[child_x][child_y]==0 || visit[child_x][child_y]==2){
                    my_deq.push_back({child_x,child_y});
                    visit[child_x][child_y]=3;//이거 안하면 중복자식담음
                    
                }
                
            }
            
        }
    }
}

//벽 3개를 새우는 백트래킹 + DFS
void wall(std::vector<std::vector<int>>& visit,int deep=0){
    void DFS(std::vector<std::vector<int>>&,int,int);//DFS함수 선언
    
    if (deep==3){
        result=0;
        std::vector<std::vector<int>> previsit;
        previsit.assign(n,std::vector<int>(m));
        std::copy(visit.begin(), visit.end(),previsit.begin());
        
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                if (visit[i][j]==2){
                    DFS(visit,i,j);
                    
                    
                }
                
            }
            
        }
        
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                if (visit[i][j]==0){
                    result+=1;
                    
                }
            }
            
        }
        
//        std::cout<<result;
//        if(result>100){std::cout<<"error";exit(0);}
        if(result>Answer){
            Answer=result;
        }
        std::copy(previsit.begin(), previsit.end(),visit.begin());
        return;
    }
    
    
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            if (visit[i][j]==0){
                visit[i][j]=1;
                wall(visit,deep+1);
                visit[i][j]=0;
                
            }
        }
    }

}
