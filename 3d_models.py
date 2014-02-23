#!/usr/bin/env python
import numpy
from numpy import sin,cos,pi,arctan,power,sign
import mayavi
from numpy.random import uniform
from mayavi import mlab
u,v=numpy.mgrid[0:2*pi:160j,0:2*pi:160j]
class tocke():
    def Xx(self,R,r,v,u):
        x=(R+r*cos(v))*cos(u)
        y=(R+r*cos(v))*sin(u)
        z=r*sin(v)
        return x,y,z
    def Nn(self,R,r,v,u):
        xv=cos(u)*(-r)*sin(v)
        yv=sin(u)*(-r)*sin(v)
        zv=r*cos(v)
        xu=-(R+cos(v)*r)*sin(u)
        yu=(R+cos(v)*r)*cos(u)
        zu=zv*0
        for a in range(160):
            for b in range(160):
                aa=numpy.array([xu[a][b],yu[a][b],zu[a][b]])
                bb=numpy.array([xv[a][b],yv[a][b],zv[a][b]])
                cro=numpy.cross(aa,bb)
                pomocna=1/numpy.linalg.norm(cro)
                print pomocna.shape
                cro=pomocna*cro
                xu[a][b],yu[a][b],zu[a][b]=cro
        return xu,yu,zu
    def Ff(self,m,n,v,u):
        zbroj=u*0
        gl_zbroj=zbroj*0
        for i in range(n):
            zbroj=u*0
            for j in range(m):
                a=uniform(-1,1)*cos(i*u+2*pi*uniform(0,1))
                b=cos(j*v+2*pi*uniform(0,1))
                zbroj=zbroj+(a*b)
            gl_zbroj=gl_zbroj+zbroj
        return gl_zbroj
    def Ss(self,V,e):
        vrati=sign(V)*power((2/pi)*arctan(abs(V)),e)
        return vrati
def pokreni():
    #fiksni manji polumjer
    toc=tocke()
    x,y,z=toc.Xx(10,3,v,u)
    mlab.mesh(x,y,z,extent=(0,0,0,0,0,0),colormap='gist_earth')
    #varijabilni manji polumjer
    r=power(sin(u/2),2)*3
    x,y,z=toc.Xx(10,r,v,u)
    mlab.mesh(x,y,z,extent=(0,0,-30,-30,0,0),colormap='gist_earth')
    #svijanje torusa
    x,y,z=toc.Xx(10,3,v,u)+2*abs(sin(5*u)+sin(3*v))*toc.Nn(10,3,v,u)
    mlab.mesh(x,y,z,extent=(0,0,30,30,0,0),colormap='gist_earth')
    #random svijanje torusa
    x,y,z=toc.Xx(10,3,v,u)+0.2*toc.Ff(6,12,v,u)*toc.Nn(10,3,v,u)
    mlab.mesh(x,y,z,extent=(-30,-30,0,0,0,0),colormap='gist_earth')
    #random svijanje torusa
    x,y,z=toc.Xx(10,3,v,u)+1*toc.Ss(toc.Ff(6,12,v,u)*toc.Nn(10,3,v,u),0.5)
    mlab.mesh(x,y,z,extent=(30,30,0,0,0,0),colormap='gist_earth')
    mlab.show()
pokreni()
