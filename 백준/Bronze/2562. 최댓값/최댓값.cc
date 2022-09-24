#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
void my_print(int n){cout<<n<<"\n";}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    /*-----------code-----------------*/
    int max_val,max_itr;
    max_val=-1;max_itr=-1;
    for(int i=0;i<9;i++){
        int new_num;
        cin>>new_num;
        if (new_num>max_val){max_val=new_num;max_itr=i;}
    }

    cout<<max_val<<"\n"<<max_itr+1;


    
    /*-----------code-----------------*/
    return 0;
}
