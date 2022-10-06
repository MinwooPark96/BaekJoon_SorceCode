//
//  main.cpp
//  BaekJoon
//
//  Created by Minwoo on 2022/09/23.
//
#include <iostream>
#include <vector>
#include <algorithm>
//#include <set>
#include <map>
//#include <unordered_map>
#include <deque>
#include <list>

//using std::cout;
//using std::cin;

// 백준 20055 번


/*------------------function------------*/






/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    /*-----------code-----------------*/
    int N,K;std::cin>>N>>K;
    int level=0;
    int start_idx=0;
    
    std::vector<int> durability(2*N,0);
    std::deque<int> robot(N,0);
    for (int i=0;i<2*N;i++){
        std::cin>>durability[i];
    }
    
    while (true){
        level+=1;
        //step 1
        start_idx-=1;if(start_idx<0){start_idx+=2*N;}
        
        robot.pop_back();
        robot.push_front(0);
        if(robot[N-1]){robot[N-1]=0;}
        //step 2
        for (int i=N-2;i>=0;i--){
            if(robot[i]==1 && robot[i+1]==0 && durability[(start_idx+i+1)%(2*N)]>=1){
                durability[(start_idx+i+1)%(2*N)]-=1;
                robot[i]=0;
                robot[i+1]=1;
            }
            
        
        if(robot[N-1]){robot[N-1]=0;}
    }
    
    
    
    //step 3
    if (durability[start_idx]>0){
        durability[start_idx]-=1;
        robot[0]=1;
    }
    //step 4
    if (std::count(durability.begin(), durability.end(), 0)>=K){
        std::cout<<level;
        break;
    }
    

    }
    
    
    
    /*-----------code-----------------*/
    return 0;
}

