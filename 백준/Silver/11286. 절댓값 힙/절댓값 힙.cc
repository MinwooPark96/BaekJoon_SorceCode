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

int N;
int n=0;
std::vector<int> heap(1,-1);

void swap(int idx1,int idx2){
    int temp=heap[idx1];
    heap[idx1]=heap[idx2];
    heap[idx2]=temp;
    
}

int abs(int value){
    if (value>0){
        return value;
    }
    return value*(-1);
    
}


void Heapify(int idx){
    int left=idx*2;
    int right=idx*2+1;
    int minest_idx;
    if (left>n || n<=1) {return;}
    
    
    if (abs(heap[idx])>abs(heap[left]) && left<=n){
        minest_idx=left;
    }
    else if (abs(heap[idx])==abs(heap[left]) && left<=n){
        if (heap[idx]>heap[left]){
            minest_idx=left;
        }
        else{
            minest_idx=idx;
        }
    }
    
    else {
        minest_idx=idx;
    }
    
    if (abs(heap[minest_idx])>abs(heap[right]) && right<=n){
        minest_idx=right;
    }
    else if (abs(heap[minest_idx])==abs(heap[right]) && right<=n){
        if (heap[minest_idx]>heap[right]){
            minest_idx=right;
        }
    }
    
    
    if (minest_idx!=idx){
        swap(minest_idx,idx);
        Heapify(minest_idx);
    }
}


void Decrease(int new_value){ //abs(new_value)<abs(value)
    int idx=n;
    heap[idx]=new_value;
    
    while (idx!=1 && abs(heap[idx/2])>=abs(heap[idx])){
        if (abs(heap[idx/2])>abs(heap[idx])){
            swap(idx,idx/2);
            
        }
        else {
            if (heap[idx/2]>heap[idx]){
                swap(idx,idx/2);
                
            }
        }
        idx=idx/2;
        
    }
    
}


void Insert(int value){
    n++;
    heap.push_back(2147483647);
    Decrease(value);
}


int Pop(){
    swap(1,n);
    int result=heap.back();
    heap.pop_back();
    n--;
    Heapify(1);
    return result;
    
    
}











/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    
    
    
    /*-----------code-----------------*/
    std::cin>>N;
    for (int i=0;i<N;i++){
        int operate;
        std::cin>>operate;
        if (operate==0){
            if (n==0){
                std::cout<<0<<'\n';
            }
            else{
                std::cout<<Pop()<<'\n';
                
            }
        }
        else{
            Insert(operate);
        }
    }
    
    
    
    
    
    /*-----------code-----------------*/

    
    
    return 0;
    
}

/*------------------function------------*/



/*-------------function-----------------*/

