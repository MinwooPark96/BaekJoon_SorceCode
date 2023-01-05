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
    
    std::vector<float> array;
    int n; input(n);
    rep(i,0,n){
        int x;
        input(x);
        array.push_back(x);
    }
    
    std::sort(array.begin(), array.end(), [](float a, float b){return a < b;});
    float max_value = array[n-1];
    float new_num;
    float sum_num = 0;
    rep(i,0,n){
        new_num = array[i]/max_value * 100;
        sum_num += new_num;
    }
    print(sum_num/n);
    
    
    /*-----------code-----------------*/
    
    
    
    return 0;
    
}
/*------------------function------------*/



/*-------------function-----------------*/

