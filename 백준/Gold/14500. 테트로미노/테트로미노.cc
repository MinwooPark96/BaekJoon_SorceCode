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

// 백준 14500 번


/*------------------function------------*/
//정답 변수

int result=0;
int answer=0;


// rotation function (90)
std::vector<std::vector<int>> rotation(const std::vector<std::vector<int>>& matrix){
    int n=(int)matrix.size();
    int m=(int)matrix[0].size();
    
    std::vector<std::vector<int>> result;
    result.assign(m, std::vector<int>(n,-1));
    
    for (int j=0;j<m;j++){
        for (int i=n-1;i>=0;i--){
            result[j][i]=matrix[n-1-i][j];
        }
    }
    
    return result;
}

// flip function (90)
std::vector<std::vector<int>> flip(const std::vector<std::vector<int>>& matrix){
    int n=(int)matrix.size();
    int m=(int)matrix[0].size();
    
    std::vector<std::vector<int>> result;
    result.assign(n, std::vector<int>(m,-1));
    
    for (auto i=0;i<n;i++){
        for (auto j=0;j<m;j++){
            result[i][j]=matrix[i][m-1-j];
        }
    }
    
    return result;
}


void sliding(const std::vector<std::vector<int>>&matrix,const std::vector<std::vector<int>>& window){
    int n=(int)matrix.size();int m=(int)matrix[0].size(); //matrix size
    int x=(int)window.size();int y=(int)window[0].size();
    
    for (int i=0;i<n-x+1;i++){
        for (int j=0;j<m-y+1;j++){
            //i,j is start point
            //sliding start;
            
            for (int a=0;a<x;a++){
                for (int b=0;b<y;b++){
                    result+=matrix[i+a][j+b]*window[a][b];
                    
                }
            }
            if (result>answer){
                answer=result;
                
            }
            result=0;
        }
    }//sliding end
}






/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    /*-----------code-----------------*/
    
    //입력받는 구간
    int n,m;std::cin>>n>>m;
    std::vector<std::vector<int>> matrix(n,std::vector<int>(m,0));

    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            std::cin>>matrix[i][j];
        }
    }

    
    //기본 모양틀 만들기.
    std::vector<std::vector<int>> line(1,std::vector<int>(4,1));
    std::vector<std::vector<int>> square(2,std::vector<int>(2,1));
    //아래 3개 틀은 구체적 구현 해야함.
    std::vector<std::vector<int>> chair(3,std::vector<int>(2,0));
    std::vector<std::vector<int>> duck(3,std::vector<int>(2,0));
    std::vector<std::vector<int>> fuck(2,std::vector<int>(3,0));

    chair[0][0]=1;chair[1][0]=1;chair[2][0]=1;chair[2][1]=1;
    duck[0][0]=1;duck[1][0]=1;duck[1][1]=1;duck[2][1]=1;
    fuck[0]={1,1,1}; fuck[1][1]=1;

    
    //line : 2개
    sliding(matrix, line);
    
    auto line2=rotation(line);
    sliding(matrix,line2);
    //square : 1개
    sliding(matrix, square);
    //chair : 8개
    
    for (int i=0;i<4;i++){
        
        sliding(matrix,chair);
        chair=rotation(chair);
        
    }
    chair=flip(chair);
    for (int i=0;i<4;i++){
        
        sliding(matrix,chair);
        chair=rotation(chair);
        
    }
    //duck : 4개
    for (int i=0;i<4;i++){
        
        sliding(matrix, duck);
        duck=rotation(duck);
        
    }
    duck=flip(duck);
    //duck : 4개
    for (int i=0;i<4;i++){
        
        sliding(matrix, duck);
        duck=rotation(duck);
        
    }
    
    //fuck : 4개
    for (int i=0;i<4;i++){
        
        sliding(matrix, fuck);
        fuck=rotation(fuck);
        
    }
    
    std::cout<<answer;


    /*-----------code-----------------*/

    
    return 0;
}

/*------------------function------------*/



















/*-------------function-----------------*/
