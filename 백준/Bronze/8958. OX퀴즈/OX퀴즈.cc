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
    
    std::string s;
    int n;
    input(n);
    rep(l,0,n){
        input(s);
        int size = (int) s.length();
        int answer = 0;
        int point = 0;
        rep (i,0,size){
            if (s[i] == 'O'){
                point += 1;
                answer += point;
            }
            else {
                point = 0;
            }
        }
        print(answer);
    }
    /*-----------code-----------------*/
    
    
    
    return 0;
    
}
/*------------------function------------*/



/*-------------function-----------------*/

