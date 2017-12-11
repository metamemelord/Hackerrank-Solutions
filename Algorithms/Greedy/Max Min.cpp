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
    int w;
    cin>>w;
    int i;
    vector<int> x(n);
    for(i=0;i<n;i++)
        cin>>x[i];
    sort(x.begin(),x.end());
    int ans = INT_MAX;
    for(i=0;i<=n-w;i++)
        ans = min(ans,x[i+w-1]-x[i]);
    cout<<ans;
}
