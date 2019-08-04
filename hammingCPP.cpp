#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

string hamming(string s){
  string ar[4];
  ""
  int iP1=0,iP2=1,iP4=3,iP8=7;
  
  while(iP1<s.length()-1){
    calculateIP(ar[0],s,1,iP1);
    calculateIP(ar[1],s,2,iP2);
    
    calculateIP(ar[2],s,4,iP4);
    calculateIP(ar[3],s,8,iP8);


    iP1+=2;
    iP2+=4;
    iP4+=8;
    iP8+=16;
  }
  cout<<ar[0]<<endl<<ar[1]<<endl<<ar[2]<<endl<<ar[3]<<endl;
  cout<<s<<endl;
  s[0]=(ar[0].length()%2==0) ? '0' : '1';
  s[1]=(ar[1].length()%2==0) ? '0' : '1';
  s[3]=(ar[2].length()%2==0) ? '0' : '1';
  s[7]=(ar[3].length()%2==0) ? '0' : '1';
  
  return s;

}

void calculateIP(string & s, string sCode,int iP, int control){
  if(iP>0){
    if(control<sCode.length()){
      s+=sCode[control];
      calculateIP(s,sCode,iP-1,control+1);
    }
  }
}



int main(){
  string test="??0?100?1101";
  cout<<hamming(test);


  return 0;
}