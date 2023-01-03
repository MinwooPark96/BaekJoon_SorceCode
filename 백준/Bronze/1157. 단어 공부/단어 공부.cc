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
    
    std::vector<int> a(26,0);
    std::vector<int> b;
    std::string s;
    
    input(s);
    
    rep(i,0,s.size()){
        int x = s[i];
        int th = 'A';
        int de = 'a';
        if (x < de){
            x = x-th;
        }
        else {
            x = x - de;
        }
        a[x]+=1;

    }
    int max_num;
    max_num=*std::max_element(a.begin(), a.end());
    rep(i,0,26){
        if (a[i]==max_num){
            b.push_back(i);
        }
    }
    if (b.size() != 1) {
        std::cout<<'?';
    }
    
    else {
        char answer = b[0] + 'A';
        print(answer);
    }
    
    
    /*-----------code-----------------*/
    
    
    
    return 0;
    
}
/*------------------function------------*/



/*-------------function-----------------*/

