#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;
void my_print(int n){cout<<n<<"\n";}

/*------------------function------------*/
template <class T> double average(vector<T> my_vec){
    int sum=0;
    float my_vec_size=my_vec.size();
    for(int i=0;i<my_vec_size;i++){
        sum+=my_vec[i];
    }
    return sum/my_vec_size;
}

void percent(void){
    
    int n;cin>>n;
    vector<int> my_vec;
    for (int i=0;i<n;i++){
        int new_num;cin>>new_num;
        my_vec.push_back(new_num);
    }
    double my_avg=average(my_vec);
    int count=0;
    for (int i=0;i<n;i++){
        if(my_vec[i]>my_avg) count+=1;
    }
    cout.precision(3);
    cout<<fixed<<count*100.0/my_vec.size()<<"%\n";
}
/*------------------------------*/
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    /*-----------code-----------------*/
    int N;
    cin>>N;
    for (int i=0;i<N;i++){
        percent();
    }
    
    
    /*-----------code-----------------*/
    return 0;
}
