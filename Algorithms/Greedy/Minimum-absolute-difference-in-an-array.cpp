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
    int n;
    cin>>n;
    vector<int> x(n);
    for(int i=0;i<n;i++)
        cin>>x[i];
    sort(x.begin(),x.end());
    int ans = abs(x[1]-x[0]);
    for(int i=1;i<n-1;i++)
        ans = min(ans,abs(x[i]-x[i+1]));
    cout<<ans<<endl;
}
