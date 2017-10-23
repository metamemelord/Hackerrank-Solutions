/*
# -*- coding: utf-8 -*-
"""
@author: MetaMemeLord-
"""
*/

#include<iostream>
#include<map>
#include<vector>
#include<queue>
#include<algorithm>
#include<stdio.h>
#include<cstring>
#include<climits>

#define mp make_pair
#define pb push_back

using namespace std;

void printMap(map<pair<int,int>,int> m)
{
    map<pair<int,int>,int>::iterator it;
    for(it = m.begin();it != m.end();it++)
        cout<<endl<<it->first.first<<','<<it->first.second<<" : "<<it->second;
    cout<<endl;
}

int main()
{
    std::ios::sync_with_stdio(false);
    int q,n,e,v1,v2,c,src,next,w1,w2;
    map<pair<int,int>,int>::iterator it;
    cin>>q;
    while(q>0)
    {
        q--;
        cin>>n>>e;
        vector<int> x[10005];
        vector<int> cost(n);
        fill(cost.begin(),cost.end(),INT_MAX);
        bool done[n];
        memset(&done,true,n*sizeof(bool));
        map<pair<int,int>,int> weight;
        pair<int,int> p;
        while(e>0)
        {
            e--;
            cin>>v1>>v2>>c;
            v1--;
            v2--;
            x[v1].pb(v2);
            x[v2].pb(v1);
            if(v1>v2)
                swap(v1,v2);
            it = weight.find(mp(v1,v2));
            if(it!=weight.end()) weight[mp(v1,v2)] = min(weight[mp(v1,v2)],c);
            else weight[mp(v1,v2)] = c;
        }
        //printMap(weight);
        priority_queue<pair<int,int>,vector<pair<int,int> > ,greater<pair<int,int> >> PQ;
        cin>>src;
        src--;
        PQ.push(mp(0,src));
        while(!PQ.empty())
        {
            p = PQ.top();
            PQ.pop();
            if(!done[p.second])
            {
                continue;
            }
            done[p.second] = false;
            cost[p.second] = p.first;
            for(auto i:x[p.second])
                if(done[i])
                {
                    w1 = i;
                    w2 = p.second;
                    if(w1>w2)
                    {
                        swap(w1,w2);
                    }
                    PQ.push(mp(min(cost[i], cost[p.second] + weight[mp(w1,w2)]),i));
                }
        }
        for(int i=0;i<n;i++)
        {
            if(i == src) continue;
            if(cost[i] == INT_MAX) cout<<-1<<' ';
            else cout<<cost[i]<<' ';
        }
        cout<<endl;
        //for(int i=0;i<n;i++)
        //    cout<<done[i]<<' ';
    }
return 0;
}
