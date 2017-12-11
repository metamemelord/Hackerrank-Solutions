/*
# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
*/

#include <bits/stdc++.h>

using namespace std;

bool degen(int a, int b, int c) {return (a+b)<=c || (b+c)<=a || (c+a)<=b;}

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n,i,j,k,l;
    cin>>n;
    vector<int> x(n);
    for(i=0;i<n;i++) cin>>x[i];
    sort(x.rbegin(),x.rend());
    bool check = true;
    for(j=0;j<n;j++)
    {
        for(k=j+1;k<n;k++)
        {
            for(l=k+1;l<n;l++)
            {
                if(!degen(x[j],x[l],x[k]))
                {
                    check = false; break;
                }
            }
            if(!check)
                break;
        }
        if(!check)
            break;
    }
    if(check) cout<<-1<<endl;
    else cout<<x[l]<<" "<<x[k]<<" "<<x[j];

    return 0;
}
