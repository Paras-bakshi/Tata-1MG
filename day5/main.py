def total_cost_per_item(items,cost_per_unit):
    cost_per_item={}
    len(cost_per_unit)
    for x in range(0,len(cost_per_unit)):
        cost_per_item[items[x][0]]=items[x][1]*cost_per_unit[x]
    return cost_per_item

def total_time_per_item(items,time_per_unit):
    time_per_item={}
    d_total = 0;h_total = 0;m_total = 0;
    for x in range(0,len(time_per_unit)):
        l = time_per_unit[x].split("/")
        h=0;m=0;d=0
        for y in range(0,len(l)):
            if(l[y][-1]=='h'):
                h = int(l[y][0:-1])
            if (l[y][-1] == 'm'):
                m = int(l[y][0:-1])
            if (l[y][-1] == 'd'):
                d = int(l[y][0:-1])
        h=items[x][1]*h;m=items[x][1]*m;d=items[x][1]*d
        d=d+int((h+(m/60))/24)
        h=(h+int(m/60))% 24
        m=m%60
        d_total=d_total+d;h_total=h_total+h;m_total=m_total+m;
        s=""
        if(m!=0):
            s=str(m)+"m/"
        if(h!=0):
            s=s+str(h)+"h/"
        if(d!=0):
            s=s+str(d)+"d"
        if(s[-1]=="/"):
            time_per_item[items[x][0]]=s[0:-1]
        else:
            time_per_item[items[x][0]]=s
    d_total=d_total+int((h_total+(m_total/60))/24)
    h_total=(h_total+int(m_total/60))%24
    m_total=m_total%60
    s=""
    if(m_total!=0):
        s=str(m_total)+"m/"
    if(h_total!=0):
        s=s+str(h_total)+"h/"
    if (d_total!= 0):
        s=s+str(d_total)+"d"
    if (s[-1]=="/"):
        s=s[0:-1]
    return time_per_item,s

def total_time_and_cost(items,time_per_unit,cost_per_unit):

    dict_total_cost_per_item=total_cost_per_item(items,cost_per_unit)
    total_cost=sum(list(dict_total_cost_per_item.values()))
    dict_total_time_per_item,total_time=total_time_per_item(items,time_per_unit)
    print(dict_total_cost_per_item)
    print(dict_total_time_per_item)
    print("total_cost: ",total_cost)
    print("total_time: ",total_time)

if __name__ == "__main__":
    items = [["chair", 3], ["bed", 2], ["table", 2]]
    time_per_unit = ["5h", "50m/2h/2d", "50m/6h"]
    cost_per_unit = [500, 10000, 700 ]
    total_time_and_cost(items,time_per_unit,cost_per_unit)


