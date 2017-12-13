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


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin>>n;
    int x[n];
    for(int i=0;i<n;i++)
        cin>>x[i];
    sort(x,x+n);
    int val = x[0],count = 1;
    for(int i=1;i<n;i++)
    {
        if(val+4 >= x[i])
            continue;
        val = x[i];
        count++;
    }
    cout<<count<<endl;
    return 0;
}
