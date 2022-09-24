
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;
void my_print(int n){cout<<n<<"\n";}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    /*-----------code-----------------*/
    set<int> my_set;
    set<int>::iterator iter;
    for (int i=0;i<10;i++){
        int new_num;
        cin>>new_num;
        my_set.insert(new_num%=42);
    }
    
    cout<<my_set.size();
    /*-----------code-----------------*/
    return 0;
}
