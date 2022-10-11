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
// 백준 17626 번


/*------------------function------------*/
//정답 변수


/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    /*-----------code-----------------*/
    int n;std::cin>>n;
    
    std::vector<int> square_num(n+1,0);
    square_num[1]=1;
    
    for (int target=2;target<=n;target++){
        int min_square=4;
        for (int num=1;num<=(int)sqrt(target);num++){
            if (square_num[target-num*num]+1<min_square){
                min_square=square_num[target-num*num]+1;
            }
        }
        square_num[target]=min_square;
    }
        
    
    
    std::cout<<square_num[n];
    
    
    
    
    /*-----------code-----------------*/

    
    return 0;
}

/*------------------function------------*/


