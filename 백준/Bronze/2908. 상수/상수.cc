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
#define print(x) std::cout << x <<' '
#define input(x) std::cin >> x


/*----------------macro--------------*/
/*------------------function------------*/
//정답 변수









/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    
    
    
    /*-----------code-----------------*/
    
    int a,b;input(a);input(b);
    int new_a=0;
    int new_b=0;
    int ten=100;
    while (a!=0){
        int q = a/10;
        int r = a%10;
        a= q;
        new_a += ten*r;
        ten/=10;
    }
    ten=100;
    while (b!=0){
        int q = b/10;
        int r = b%10;
        b = q;
        new_b += ten*r;
        ten/=10;
    }
    
    if (new_a > new_b){
        print(new_a);
    }
    else {
        print(new_b);
    }
    
    /*-----------code-----------------*/
    
    
    
    return 0;
    
}
/*------------------function------------*/



/*-------------function-----------------*/

