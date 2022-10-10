//
//  main.cpp
//  BaekJoon
//
//  Created by Minwoo on 2022/09/23.
//
#include <iostream>
//#include <vector>
//#include <algorithm>
//#include <set>
//#include <functional>
//#include <map>
//#include <unordered_map>
//include <deque>
//#include <list>
//#include <queue>
//using std::cout;
//using std::cin;

// 백준 14500 번


/*------------------function------------*/
//정답 변수


/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    /*-----------code-----------------*/
    
    int my_set[21]={0};
    int size=0;
    int n;std::cin>>n;
    
    for (int i=0;i<n;i++){
        std::string op; std::cin>>op;
        if (op=="add"){
            int value;std::cin>>value;
            if (my_set[value]==0){
                my_set[value]=1;
                size+=1;
            }
            
        }
            
        else if (op=="remove"){
            int value;std::cin>>value;
            if (my_set[value]==1){
                my_set[value]=0;
                size-=1;
            }
            
        }
        
        else if (op=="check"){
            int value;std::cin>>value;
            if (my_set[value]==1){
                std::cout<<1<<"\n";
            
            }
            else {
                std::cout<<0<<"\n";
            }
            
        }
        
        else if (op=="toggle"){
            int value;std::cin>>value;
            if (my_set[value]==0){
                my_set[value]=1;
                size+=1;
            }
            else {
                my_set[value]=0;
                size-=1;
            }
            
        }
        
        
        else if (op=="all"){
            for (int i=1;i<=20;i++){
                my_set[i]=1;
            }
            size=20;
            
        }
        
        else{
            for (int i=1;i<=20;i++){
                my_set[i]=0;
            }
            size=0;
            
        }
        
        
        
        
        
        
        
        
        
        
        
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    /*-----------code-----------------*/

    
    return 0;
}

/*------------------function------------*/



















/*-------------function-----------------*/

