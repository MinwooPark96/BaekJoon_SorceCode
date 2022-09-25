#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;
void my_print(int n){cout<<n<<"\n";}

/*------------------function------------*/
int count_hansu(int n){
    if (n<100) return n;
    else if (n<1000){
        int result=99;
        for (int i=100;i<=n;i++){
            int digit_1=i/100;
            int digit_2=(i%100)/10;
            int digit_3=(i%10);
            if ((digit_1+digit_3)==2*digit_2) result+=1;
        }
        return result;
        
    }
    else{
        return count_hansu(999);
    }
}


/*-------------function-----------------*/

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    /*-----------code-----------------*/
    int input;
    cin>>input;
    int answer=count_hansu(input);
    cout<<answer<<"\n";
    
    /*-----------code-----------------*/
    return 0;
}