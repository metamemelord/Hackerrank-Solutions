/*
# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define print(x) for(auto k:x) cout<<k<<" "; cout<<endl;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int i,n;
    cin>>n;
    int xa[n],xb[n],a[n],b[n];
    for(i=0;i<n;i++)
    {
        cin>>a[i];
        xa[i] = a[i];
    }
    for(i=0;i<n;i++)
    {
        cin>>b[i];
        xb[i] = b[i];
    }
    sort(xa,xa+n);
    sort(xb,xb+n);
    for(i=0;i<n;i++)
        if(xa[i] != xb[i])
            break;
    if(i==n) {cout<<n-1;return 0;}
    bool adone[n]={0},bdone[n]={0};
    int count = 0;
    for(i=0;i<n;i++)
        for(int j=0;j<n;j++)
            if(a[i] == b[j] && !adone[i] && !bdone[j])
            {
                count++;
                adone[i] = bdone[j] = 1;
                break;
            }
    cout<<count+1;
    return 0;
}
