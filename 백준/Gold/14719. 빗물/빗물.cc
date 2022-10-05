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

// 백준 14719 번
//2 20 50
//50 30
//20 40
//


/*------------------function------------*/



/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    /*-----------code-----------------*/
    int answer=0;
    int n,m;std::cin>>n>>m;
    std::vector<std::vector<int>> matrix(n,std::vector<int>(m,0));
    std::vector<std::vector<int>> visit(n,std::vector<int>(m,0));
    
    for (int j=0;j<m;j++){
        int height;std::cin>>height;
        for (int i=n-1;i>n-1-height;i--){
            matrix[i][j]=1;
            
        }
    }
    for (int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if (visit[i][j]==0){
                visit[i][j]=1;
                if(matrix[i][j]==1){
                    for (int k=j+1;k<m;k++){
                        visit[i][k]=1;
                        if(matrix[i][k]==1){
                            visit[i][k]=0;
                            answer+=k-j-1;
                            //std::cout<<i<<" "<<j<<" "<<k<<"\n";
                            break;
                        }
                    }
                }
            }
        }
    }
    std::cout<<answer;

    /*-----------code-----------------*/
    return 0;
}

