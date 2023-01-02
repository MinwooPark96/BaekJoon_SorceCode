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

/*------------------function------------*/
//정답 변수



/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    
    
    
    /*-----------code-----------------*/
    std::vector<int> array(3,0);
    int reward;
    std::cin>>array[0]>>array[1]>>array[2];
    
    if (array[0]==array[1] and array[1]==array[2]) {
        reward = 10000 + array[0]*1000;
    }
    
    else if (array[0]!=array[1]
             and array[1]!=array[2]
             and array[2]!=array[0]) {
        int max_element;
        max_element=*std::max_element(array.begin(), array.end());
        reward = max_element * 100;
        
    }
    
    else {
        if (array[0]==array[1]){
            reward = 1000 + 100*array[0];
        }
        else if (array[1]==array[2]){
            reward = 1000 + 100*array[1];
        }
        else  {
            reward = 1000 + 100*array[2];
        }
    }
    
    std::cout<<reward;
    /*-----------code-----------------*/

    
    
    return 0;
    
}

/*------------------function------------*/



/*-------------function-----------------*/

