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
#include <numeric>
#include <sstream>
/*----------------macro--------------*/

#define rep(i,a,b) for (int i = (a); i < (b); ++i)
#define debug(x) std::cout << #x << " is " << x << '\n'
#define print(x) std::cout << x <<'\n'
#define input(x) std::cin >> x


/*----------------macro--------------*/
/*------------------function------------*/
//정답 변수









/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    
    
    
    /*-----------code-----------------*/
    
    std::vector<std::vector<int>> matrix(100,std::vector<int>(100,0));
    int n; input(n);
    rep(i,0,n){
        int a,b;
        input(a); input(b);
        rep(j,a,a+10){
            rep(k,b,b+10){
                matrix[j][k]=1;
            }
        }
        
    }
    int answer=0;
    rep(i,0,100){
        rep(j,0,100){
            if (matrix[i][j]==1){
                answer+=1;
            }
        }
    }
    
    print(answer);
    
    /*-----------code-----------------*/
    
    
    
    return 0;
    
}
/*------------------function------------*/



/*-------------function-----------------*/

