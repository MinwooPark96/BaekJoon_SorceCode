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
    
    int n,m;
    input(n);input(m);
    std::vector<int> A(n*m,0),B(n*m,0);
    rep(i,0,n*m){
        int x;input(x);
        A[i]=x;
    }
    rep(i,0,n*m){
        int x;
        input(x);
        B[i]=x;
    }
    
    rep(i,0,n*m){
        A[i]=A[i]+B[i];
    }
    
    rep(i,0,n){
        rep(j,0,m){
            print(A[m*i+j]);
            print(' ');
        }
        std::cout<<'\n';
    }
    
    
    /*-----------code-----------------*/
    
    
    
    return 0;
    
}
/*------------------function------------*/



/*-------------function-----------------*/

