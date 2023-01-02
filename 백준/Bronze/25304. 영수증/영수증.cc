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

/*----------------macro--------------*/

#define rep(i,a,b) for (int i = (a); i < (b); ++i)
#define debug(x) std::cout << #x << " is " << x << '\n'
#define print(x) std::cout << x << '\n'
#define input(x) std::cin >> x

/*----------------macro--------------*/
/*------------------function------------*/
//정답 변수









/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    
    
    
    /*-----------code-----------------*/
    int total = 0;
    int sum = 0;
    input(total);
    int n;
    input(n);
    rep(i,0,n){
        int price,num;
        input(price); input(num);
        sum += price*num;
        
    }
    
    if (sum==total){
        print("Yes");
    }
    else {
        print("No");
    }
    
    /*-----------code-----------------*/

    
    
    return 0;
    
}

/*------------------function------------*/



/*-------------function-----------------*/

