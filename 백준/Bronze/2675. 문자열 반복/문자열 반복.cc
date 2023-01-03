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
#define print(x) std::cout << x
#define input(x) std::cin >> x


/*----------------macro--------------*/
/*------------------function------------*/
//정답 변수









/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    
    
    
    /*-----------code-----------------*/
    int n; input(n);
    rep(i,0,n){
        int m;input(m);
        std::string s;input(s);
        int size=(int)s.size();
        rep(j,0,size){
            rep(k,0,m){
                print(s[j]);
            }
        }
        std::cout<<'\n';
    }
        
    
    
    /*-----------code-----------------*/
    
    
    
    return 0;
    
}
/*------------------function------------*/



/*-------------function-----------------*/

