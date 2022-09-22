#include <iostream>

using namespace std;
int const maxhour=24;
int const maxmin=60;
int main(){
    int hour,min;
    cin>>hour>>min;
    
    if (min>=45) cout<<hour<<" "<<min-45<<"\n";
    else {
        if(hour==0){cout<<hour-1+maxhour<<" "<<min-45+maxmin<<"\n";}
        else{cout<<hour-1<<" "<<min-45+maxmin<<"\n";}
        }return 0;
    
    
}
