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

//0<=d<min(n,m)
int sliding(const std::vector<std::vector<int>>& my_matrix,const int& n, const int& m, const int& d){
    
    int start_x=-1;
    int start_y=0;
    for (int i=0;i<n-(d);i++){
        start_x++;
        start_y=0;
        for (int j=0;j<m-(d);j++){
            if (my_matrix.at(start_x).at(start_y)== my_matrix.at(start_x+d).at(start_y)&&
                my_matrix.at(start_x).at(start_y)==my_matrix.at(start_x).at(start_y+d)&&
                my_matrix.at(start_x).at(start_y)==my_matrix.at(start_x+d).at(start_y+d)){
                
                return (d+1)*(d+1);
            }
            start_y++;
                
        }
    }
    return -1;
}








/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    /*-----------code-----------------*/
    int n;std::cin>>n;int m;std::cin>>m;
    std::vector<std::vector<int>> my_matrix(n,std::vector<int>(m,0));
    
    for (int i=0;i<n;i++){
        std::string nums;
        std::cin>>nums;
        for (int j=0;j<m;j++){
            my_matrix[i][j]=(int)(nums[j]-'0');
        }
    }
    
    for (int l=std::min(n,m)-1;l!=-1;l--){
        int answer=sliding(my_matrix, n, m, l);
        if (answer!=-1){std::cout<<answer;break;}
    }
    
    /*-----------code-----------------*/
    return 0;
}