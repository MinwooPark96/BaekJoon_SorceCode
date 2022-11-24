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

int V;
int E;
//std::vector<std::vector<long>> weight;
long minimum_weight=0;


//우선 union find 를 구현 해서 두 정점간에 cycle 이 있는지 없는지 판단할 수 있어야 한다.
std::vector<int> parent;

int get_parent(int x){
    if (parent[x]==x){
        return x;
    }
    return get_parent(parent[x]);
}
    
// 노드를 직접 연결하는 것이 아닌 부모를 합치는 과정임을 주의하라.
void union_parent(int x,int y){
    int parent_x=get_parent(x);
    int parent_y=get_parent(y);
    
    if (parent_x<parent_y){
        parent[parent_y]=parent_x;
    }
    else {
        parent[parent_x]=parent_y;
    }
}

// 두 노드의 부모가 같은지 확인하라.
bool find_parent(int x, int y){
    int parent_x=get_parent(x);
    int parent_y=get_parent(y);
    if (parent_x==parent_y){
        return true;
    }
    return false;
}


class edge_info{
public:
    long weight=0;
    int v1=0;
    int v2=0;
    edge_info(long _weight,int _v1,int _v2){
        weight=_weight;
        v1=_v1;
        v2=_v2;
    }
};


bool compare_edge(edge_info a, edge_info b){
    if (a.weight<b.weight){
        return true;
    }
    else return false;
}



/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    
    
    
    /*-----------code-----------------*/
    
    
    std::cin>>V;
    std::cin>>E;
    
//   weight 값 받아오기
//    weight.assign(V, std::vector<long>(V,0));
//    for (int r=0;r<V;r++){
//        for (int c=0;c<V;c++ ){
//            long new_weight;
//            std::cin>>new_weight;
//            weight[r][c]=new_weight;
//        }
//    }

    
    //   parent 초기화
    for (int i=0;i<=V;i++){
        parent.push_back(i);
    }

//   edge 별 클래스 생성
    std::vector<edge_info> edge;
    for (int e=0;e<E;e++){
        int _v1;std::cin>>_v1;
        int _v2;std::cin>>_v2;
        long new_weight;std::cin>>new_weight;
        
        edge.push_back(edge_info(new_weight,_v1,_v2));
    }
    
    // edge 를 weight 로 오름차순 정렬
    
    std::sort(edge.begin(), edge.end(), compare_edge);
    int count=0;
    for (edge_info e:edge){
        if (find_parent(e.v1, e.v2)){
            continue;
        }
        if (count>V-1 || count>E){
            break;
        }
        else {
            union_parent(e.v1,e.v2);
            minimum_weight+=e.weight;
            count+=1;
        }
        
    }
    
    std::cout<<minimum_weight;
    
    
    
    
    
    
    
    
    /*-----------code-----------------*/

    
    
    return 0;
    
}

/*------------------function------------*/



/*-------------function-----------------*/
