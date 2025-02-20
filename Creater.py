def DrawCircle(r):
    function_name = "drawcircle_"+str(r)
    fp = open(function_name +".mcfunction",'w')
    for i in range(0,20*r):
        fp.write("particle end_rod ~ ~ ~ {0:.10f} 0 {1:.10f} {2:.10f} 0 force @a \n".format(math.cos(i/10/r*math.pi),math.sin(i/10/r*math.pi),r/12))
    fp.close()
def DrawLine(dx,dy,dz,tick):
    function_name = "drawline_"+str(dx)+'_'+str(dy)+'_'+str(dz)+'_'+str(tick)
    n=max(abs(dx),abs(dy),abs(dz))*10
    fpmain=open(function_name+"_main.mcfunction",'w')
    for t in range(0,tick):
        fp =open(function_name+'_'+str(t)+".mcfunction",'w')
        for i in range(n*t//tick,n*(t+1)//tick):
            fp.write("particle end_rod ~{0:.10f} ~{1:.10f} ~{2:.10f} 0 0 0 0 0 force @a\n".format(dx/n*i,dy/n*i,dz/n*i))
        fp.close()
        fpmain.write("schedule function music:"+function_name+'_'+str(t)+" "+str(t)+"t\n")
    fpmain.close
def Drawcube():
    fp=open("drawcube.mcfunction",'w')
    for i in range(0,17):
        fp.write('''particle end_rod ~-0.5 ~-0.5 ~{0:.10f} 0 0.5 0 0.08333 0 force @a
particle end_rod ~0.5 ~-0.5 ~{0:.10f} 0 0.5 0 0.08333 0 force @a
particle end_rod ~-0.5 ~0.5 ~{0:.10f} 0 0.5 0 0.08333 0 force @a
particle end_rod ~0.5 ~0.5 ~{0:.10f} 0 0.5 0 0.08333 0 force @a
particle end_rod ~-0.5 ~{0:.10f} ~-0.5 0 0.5 0 0.08333 0 force @a
particle end_rod ~-0.5 ~{0:.10f} ~0.5 0 0.5 0 0.08333 0 force @a
particle end_rod ~0.5 ~{0:.10f} ~0.5 0 0.5 0 0.08333 0 force @a
particle end_rod ~0.5 ~{0:.10f} ~-0.5 0 0.5 0 0.08333 0 force @a
particle end_rod ~{0:.10f} ~0.5 ~-0.5 0 0.5 0 0.08333 0 force @a
particle end_rod ~{0:.10f} ~0.5 ~0.5 0 0.5 0 0.08333 0 force @a
particle end_rod ~{0:.10f} ~-0.5 ~0.5 0 0.5 0 0.08333 0 force @a
particle end_rod ~{0:.10f} ~-0.5 ~-0.5 0 0.5 0 0.08333 0 force @a
'''.format(i/16-0.5))
    fp.close
