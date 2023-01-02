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
#define print(x) std::cout << x <<'\n'
#define input(x) std::cin >> x


/*----------------macro--------------*/
/*------------------function------------*/
//정답 변수

int cycle=0;

int change(int n){
    cycle++;
    if (n<10){
        return n*10 + n;
    }
    int a,b,c;
    a=n/10;
    b=n%10;
    c=a+b;
    c=c%10;
    return 10*b+c;
    
}









/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    
    
    
    /*-----------code-----------------*/
    int n; input(n);
    int x=n;
    while (true){
        x=change(x);
        if (x==n){
            break;
        }
    }
    print(cycle);
    /*-----------code-----------------*/
    
    
    
    return 0;
    
}
/*------------------function------------*/



/*-------------function-----------------*/

