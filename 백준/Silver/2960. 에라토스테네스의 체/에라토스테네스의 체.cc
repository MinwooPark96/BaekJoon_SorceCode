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
//#include <deque>
#include <list>

//using std::cout;
//using std::cin;

// 백준 14503 번

/*------------------function------------*/

class mine{
public:
};



/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    /*-----------code-----------------*/
    int n;std::cin>>n;
    int k;std::cin>>k;
    int count=0;
    //int n=7;int k=4;
    std::vector<int> my_vec;
    for (int i=2;i<=n;i++){
        my_vec.push_back(i);
    }
    
    
    while (count<=n){
        auto min_iter=std::min_element(my_vec.begin(), my_vec.end());
        int min_value=*min_iter;
        int prime=min_value;
        int curval=prime;
        std::vector<int>::iterator finding;
        
        while (curval<=n){
            finding=std::find(my_vec.begin(),my_vec.end(),curval);
            if (*finding==curval){
                count+=1;
                my_vec.erase(finding);
                if (count==k){std::cout<<curval;exit(0);}
                }
            curval+=prime;
        }
        
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    /*-----------code-----------------*/
    return 0;
}

