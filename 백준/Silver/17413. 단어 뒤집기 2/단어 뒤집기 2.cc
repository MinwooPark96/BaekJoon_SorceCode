
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




/*-------------function-----------------*/

int main() {
    //std::ios::sync_with_stdio(false);
    //std::cin.tie(NULL);
    
    /*-----------code-----------------*/

    std::string my_str;
    std::string::iterator iter;
    std::deque<char> my_deque;
    
    
    getline(std::cin,my_str);
    bool button=true;
    for (iter=my_str.begin();iter!=my_str.end();iter++){
        char curchar=*iter;
        if (curchar=='>'){
            button=true;
            std::cout<<curchar;
            continue;
        }
        
        if (!button) {
            std::cout<<curchar;
            continue;
            
        }
        
        if (curchar=='<') {
            if(!my_deque.empty()){
                while(!my_deque.empty()) {
                    std::cout<<my_deque.back();
                    my_deque.pop_back();}
            }
            
            button=false;
            std::cout<<curchar;
            
        }
        
        else if (curchar==' ' && !my_deque.empty()){
            while(!my_deque.empty()) {
                std::cout<<my_deque.back();
                my_deque.pop_back();
            }
            std::cout<<' ';
        }
        else {my_deque.push_back(curchar);}
        
    }
    while(!my_deque.empty()) {
        std::cout<<my_deque.back();
        my_deque.pop_back();
    }
    
    
    
    
    
    /*-----------code-----------------*/
    
    return 0;
}
