/*
 -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
*/
#include<iostream>
#include<string>
#include<vector>

using namespace std;

string reverse(string s)
{
    for(int i=0,j=s.size()-1;i<s.size()/2;i++,j--)
    {
        char temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }
    return s;
}
int main()
{
    int n,i;
    string s;
    cin>>n;
    while(n>0)
    {
        n--;
        cin>>s;
        for(i=s.size()-1;i>0;i--)
            if(s[i-1] < s[i])
                break;
        if(i==0)
        {
            cout<<"no answer"<<endl;
            continue;
        }
        int ind1 = i-1;
        for(i=s.size()-1;i>ind1;i--)
            if(s[ind1] < s[i])
                break;
        //cout<<i;
        char temp = s[ind1];
        s[ind1] = s[i];
        s[i] = temp;
        string k = s.substr(ind1+1,s.size()-ind1-1);
        k = reverse(k);
        s.resize(ind1+1);
        s.append(k);
        cout<<s<<endl;
    }
    return 0;
}
