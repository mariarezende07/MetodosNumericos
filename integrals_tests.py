from random import gauss
from integrals import *
# EX 1
def volume_cubo(aresta, nos):
    volume = gauss_formula([0,aresta,"0",str(aresta)],"1", nos)
    return volume

def volume_tetraedro(vertices, nos):

    v_1 = np.subtract(vertices[2],vertices[1])
    v_2 = np.subtract(vertices[3],vertices[1])
    n = np.cross(v_1,v_2)
    d = np.dot(n,vertices[1]) 
    
    plane_equation = "("+ str(n[0]) + "* x +" + str(n[1]) + "* y -(" + str(d) + "))/"+ str(-n[2])
    
    y_var = str(d) + "-" + str(vertices[1][0]) + "* x"
    volume = gauss_formula([0,vertices[1][0],str(vertices[0][1]),str(y_var)],plane_equation, nos)
    return volume

# EX 2
def area_from_curves(curve, limits_1, limits_2, nodes):
    volume_1 = gauss_formula(limits_1,curve,nodes)
    limits_2[3] = limits_2[3].replace("y", "x")
    volume_2 = gauss_formula(limits_2,curve,nodes)
    return volume_1, volume_2

# EX 3
def superficie(plane, limits):
    exponent = str(plane[0]) + "* (x**"+str(plane[1])+")*"+str(plane[2]) + "* (y**"+str(plane[3])+")"
    partial_x = str(plane[0]) + "*" +str(plane[1]) + "*(x**" + str(plane[1] - 1) +")* (y**"+str(plane[3]) +")*" + str(plane[2])
    partial_y = str(plane[2]) + "*" +str(plane[3]) + "*(y**" + str(plane[3] - 1) +")* (x**"+str(plane[1]) +")*" + str(plane[0])
    
    area_equation = "np.sqrt(("+partial_x+"*np.exp("+exponent+"))**2 + (("+partial_y+"*np.exp("+exponent+"))**2 + 1))"
    
    area = gauss_formula(limits, area_equation, n6)
    volume = gauss_formula(limits, "np.exp("+exponent+")", n6)
    return area, volume
    
# EX 4



print(superficie([1,-1,1,1],[0.1,0.5,"x**3","x**2"]))
