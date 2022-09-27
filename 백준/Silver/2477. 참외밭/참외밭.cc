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
#include <map>
#include <unordered_map>
#include <deque>


//using std::cout;
//using std::cin;
void my_print(int n){std::cout<<n<<"\n";}


/*------------------function------------*/

bool clock(const std::map<int,int>& cycle,int a, int b){
    if(!a) return 1;
        
    if(cycle.at(a)==b) return 1;
    else return 0;
}
bool horizon(int a){
    if (a<=2){
        return 1;}
    else return 0;
}

/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    /*-----------code-----------------*/
    std::map<int,int> cycle;
    cycle.insert({4,2});
    cycle.insert({2,3});
    cycle.insert({3,1});
    cycle.insert({1,4});
    
    int weight;std::cin>>weight;
    std::vector<int> dir(6);
    std::vector<int> length(6);
    int maxhor=0;
    int maxver=0;
    int minus=0;
    
    for (int i=0;i<6;i++){
        std::cin>>dir[i];
        std::cin>>length[i];
        
        bool check=clock(cycle,dir[i-1],dir[i]);
        if (!check) {minus=length[i]*length[i-1];}
            
        if (horizon(dir[i])) {if(length[i]>maxhor) maxhor=length[i];}
        
        else {if(length[i]>maxver) maxver=length[i];}
            
        }
    if (minus==0){
        minus=length[0]*length[5];
    }
    std::cout<<weight*(maxhor*maxver-minus);
    
    /*-----------code-----------------*/
    return 0;
}

