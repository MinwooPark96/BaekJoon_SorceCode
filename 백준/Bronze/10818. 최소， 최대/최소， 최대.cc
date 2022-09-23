//
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
void my_print(int n){cout<<n<<"\n";}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    /*-----------code-----------------*/
    vector<int> my_vec;
//    vector<int>::iterator iter;
    int n;
    cin>>n;
    for (int i=0;i<n;i++){int a; cin>>a; my_vec.push_back(a);}
    sort(my_vec.begin(),my_vec.end());
    
    //for_each(my_vec.begin(),my_vec.end(),my_print);
    
    cout<<my_vec[0]<<"\n"<<my_vec[n-1];
    /*-----------code-----------------*/
    return 0;
}
