/*
# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
*/

#include<bits/stdc++.h>
#define print(x,n) for(int _= 0;_<n;_++) cout<<x[_]<<" "; cout<<endl;

using namespace std;

int x[100010];
int connected[100010];

int finds(int n) { return x[n] == n ? n : x[n] = finds(x[n]);}

void unio(int a,int b)
{
    a = finds(a);
    b = finds(b);
    if(a == b) return;
    if(a > b) swap(a,b);
    connected[a] += connected[b];
    connected[b] = 0;
    x[b] = a;
    return;
}

int main()
{
    int i,n,v1,v2;
    cin>>n;
    fill(connected,connected+2*n+1,1);
    for(i=0;i<2*n;i++) x[i] = i;
    for(i=0;i<n;i++)
    {
        cin>>v1>>v2;
        unio(v1-1,v2-1);
    }
    int m=INT_MIN, mi = INT_MAX;
    for(i=0;i<2*n;i++)
    {
        if(connected[i] == 1 || connected[i] == 0) continue;
        m = max(connected[i],m);
        mi = min(connected[i],mi);
    }
    cout<<mi<<" "<<m<<endl;
    return 0;
}
