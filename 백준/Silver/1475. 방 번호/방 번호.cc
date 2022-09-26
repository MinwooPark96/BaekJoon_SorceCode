#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>

using namespace std;
//using std::cout;
//using std::cin;
void my_print(int n){cout<<n<<"\n";}

int count_ns=0;


/*------------------function------------*/

void input(int r,vector<int>& my_vec){
    if (r==9 || r==6) count_ns++;
    else my_vec[r]+=1;
}

/*-------------function-----------------*/

int main() {
    std::ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    /*-----------code-----------------*/
    int N;cin>>N;
    vector<int> my_vec(9);
    //vector<int>::iterator iter;
    
    while (N>=10){
        int r=N%10;
        input(r,my_vec);
        N/=10;
    }
    input(N,my_vec);
    auto maxval=max_element(my_vec.begin(), my_vec.end());
    
    
    count_ns=count_ns/2+count_ns%2;
    int result=max(count_ns,*maxval);
    
    cout<<result;
    
    /*-----------code-----------------*/
    
    return 0;
}

