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
class country{
public:
    country():
    gold(0),silver(0),bronze(0),name(0)
    {}
    
    int gold;
    int silver;
    int bronze;
    int name;
    
    
};

class mine{
public:
    static bool my_sort(const country c1, const country c2){
        if (c1.gold>c2.gold) return 1;
        else if (c1.gold==c2.gold){
            if(c1.silver>c2.silver) return 1;
            else if (c1.silver==c2.silver){
                if (c1.bronze>c2.bronze) return 1;
                return 0;}
            return 0;}
        return 0;};
    
    static bool compare(const country c1, const country c2){
        if (c1.gold==c2.gold && c1.silver==c2.silver && c1.bronze==c2.bronze) return 1;
        else return 0;
    }
};



/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    /*-----------code-----------------*/
    
    int N;std::cin>>N;
    int who;std::cin>>who;
    
    std::vector<country> countrys(N);
    
    for (int i=0;i<N;i++){
        int _name,_gold,_silver,_bronze;
        
        std::cin>>_name;
        std::cin>>_gold;
        std::cin>>_silver;
        std::cin>>_bronze;
        
        countrys[i].name=_name;
        countrys[i].gold=_gold;
        countrys[i].silver=_silver;
        countrys[i].bronze=_bronze;
        
    }
    
    std::sort(countrys.begin(),countrys.end(),mine::my_sort);
    
    std::map<int,int> rank;
    int rank_num=1;
    for (int i=0;i<N;i++){
        if (!i) rank[countrys[i].name]=rank_num;
        else {
            if (mine::compare(countrys[i],countrys[i-1])){ rank[countrys[i].name]=rank[countrys[i-1].name];}
            else {rank[countrys[i].name]=rank_num;}
            }
        if (countrys[i].name==who)break;
        rank_num++;
        
    }
    
    std::cout<<rank[who];
    
    
    
    
    
    
    /*-----------code-----------------*/
    return 0;
}

