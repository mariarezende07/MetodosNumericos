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
    
    eq_plano = "("+ str(n[0]) + "* x +" + str(n[1]) + "* y -(" + str(d) + "))/"+ str(-n[2])
    
    y_var = str(d) + "-" + str(vertices[1][0]) + "* x"
    volume = gauss_formula([0,vertices[1][0],str(vertices[0][1]),str(y_var)],eq_plano, nos)
    return volume

def area_from_curves(curva, limites_1, limites_2, nos):
    volume_1 = gauss_formula(limites_1,curva,nos)
    limites_2[3] = limites_2[3].replace("y", "x")
    volume_2 = gauss_formula(limites_2,curva,nos)
    return volume_1, volume_2

def superficie(plano, limites):
    exponent = str(plano[0]) + "* (x**"+str(plano[1])+")*"+str(plano[2]) + "* (y**"+str(plano[3])+")"
    partial_x = str(plano[0]) + "*" +str(plano[1]) + "*(x**" + str(plano[1] - 1) +")* (y**"+str(plano[3]) +")*" + str(plano[2])
    partial_y = str(plano[2]) + "*" +str(plano[3]) + "*(y**" + str(plano[3] - 1) +")* (x**"+str(plano[1]) +")*" + str(plano[0])
    
    area_equation = "np.sqrt(("+partial_x+"*np.exp("+exponent+"))**2 + (("+partial_y+"*np.exp("+exponent+"))**2 + 1))"
    
    area = gauss_formula(limites, area_equation, n6)
    volume = gauss_formula(limites, "np.exp("+exponent+")", n6)
    return area, volume
    
def revolucao(nos):
    return 2 * np.pi * gauss_formula([3/4,1,'0','np.sqrt(1 -(x**2))'], 'y' , nos)


def volume_solido_rev(nos):
    return 2 * np.pi * gauss_formula([-1,1,'0','np.exp(-x**2)'], 'y', nos)

print(volume_solido_rev(n6))