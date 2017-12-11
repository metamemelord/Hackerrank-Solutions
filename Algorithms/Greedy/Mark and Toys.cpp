/*
# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
*/

#include<bits/stdc++.h>

using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int i,n,k;
    vector<int> x;
    cin>>n>>k;
    for(i=0;i<n;i++)
    {
        int val;
        cin>>val;
        x.push_back(val);
    }
    sort(x.begin(),x.end());
    int count = 0;
    i = 0;
    while(1)
    {
        k -= x[i];
        i += 1;
        if (k<0)
        {
            cout<<count<<endl;
            return 0;
        }
        count += 1;
    }
    cout<<n<<endl;
    return 0;
}
