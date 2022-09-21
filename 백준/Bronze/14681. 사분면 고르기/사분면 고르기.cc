
#include <iostream>
using namespace std;
int main() {
    // insert code here...
    int a,b;
    cin>>a;
    cin>>b;
    if (a>0 and b>0) cout<<1<<"\n";
    else if (a>0 and b<0) cout<<4<<"\n";
    else if (a<0 and b<0) cout<<3<<"\n";
    else cout<<2<<"\n";
    
    return 0;
}
