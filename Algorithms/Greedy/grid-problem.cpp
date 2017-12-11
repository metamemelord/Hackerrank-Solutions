/*
# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
*/

#include<bits/stdc++.h>

using namespace std;

int main()
{
    int n,t;
    vector<string> xl;
    cin>>t;
    while(t--)
    {
        cin>>n;
        xl.resize(0);
        for(int i=0;i<n;i++)
        {
            string s;
            cin>>s;
            sort(s.begin(),s.end());
            xl.push_back(s);
        }
        bool check = 1;
        int i=0,j=0;
        for(i=0;i<n;i++)
            for(j=0;j<n-1;j++)
                if(xl[j][i] > xl[j+1][i])\
                {
                    check = false;
                    break;
                }
        if(check) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}

