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
//#include <map>
//#include <unordered_map>
#include <deque>
//#include <list>
//#include <queue>
//using std::cout;
//using std::cin;
#include <math.h>
// 백준  번


/*------------------function------------*/
//정답 변수





/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    /*-----------code-----------------*/
    int n,m;std::cin>>n>>m;
    
    int answer=0;
    int weight=1;
    while (m!=0){
        int r=m%10;
        std::cout<<n*r<<'\n';
        m=m/10;
        answer+=weight*n*r;
        weight*=10;
        
    }
    std::cout<<answer;

    
    /*-----------code-----------------*/

    
    
    return 0;
}

/*------------------function------------*/

