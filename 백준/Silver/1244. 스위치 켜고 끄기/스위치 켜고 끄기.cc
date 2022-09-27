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

void man(const int card,std::vector<bool>& my_switch){
    int temp=card;
    while (temp<=my_switch.size()-1){
        my_switch[temp]=!my_switch[temp];
        temp+=card;
    }
}

void woman(const int card,std::vector<bool>& my_switch){
    int temp1=card-1; int temp2=card+1;
    my_switch[card]=!my_switch[card];
    
    while (temp2<=my_switch.size()-1 && temp1>=1){
        if(my_switch[temp1]==my_switch[temp2]){
            my_switch[temp1]=!my_switch[temp1];
            my_switch[temp2]=!my_switch[temp2];
            temp2++;temp1--;
        }
        else {
            break;
        }
        
    }
}


/*-------------function-----------------*/

int main() {
    //std::ios::sync_with_stdio(false);
    //std::cin.tie(NULL);
    
    /*-----------code-----------------*/
    int n;std::cin>>n;
    std::vector<bool> my_switch(n+1);
    
    for (int i=1;i<=n;i++){
        bool input;
        std::cin>>input;
        my_switch[i]=input;
    }
    int m;std::cin>>m;
    
    for (int i=0; i<m ;i++){
        int sex; std::cin>>sex;
        int card; std::cin>>card;
        if (sex==1) man(card,my_switch);
        else woman(card,my_switch);
    }
    
    
    for (int i=1;i<=n;i++){
        if (i!=1 && i%20==1){
            std::cout<<"\n"<<my_switch[i]<<" ";
        }
        else{
            std::cout<<my_switch[i]<<" ";
        }
        
    }

    
    
    
    /*-----------code-----------------*/
    return 0;
}
