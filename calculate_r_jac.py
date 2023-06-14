
numpt = 4000 #количестов геометрий
dr_dx = np.zeros((numpt, 15,18))  #dr_dx[i,j] = diff(invr_i, x_j) -- якобиан
r_dist = np.zeros((numpt,15)) #матрица расстояний между атомами
geom = np.zeros((numpt, 6*3))#вектор координат атомов в виде x_1,y_1,z_1,x_2,y_2,z_2...


def compute_dist(coords,p1,p2):
    x1 = coords[p1*3+0]
    y1 = coords[p1*3+1]
    z1 = coords[p1*3+2]

    x2 = coords[p2*3+0]
    y2 = coords[p2*3+1]
    z2 = coords[p2*3+2]

    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    d32 = dist**(3.0)
    return [dist,-(x1-x2)/d32,-(y1-y2)/d32,-(z1-z2)/d32,(x1-x2)/d32,(y1-y2)/d32,(z1-z2)/d32]






Nat = 6
ctr = 0

for k in range(numpt):
    ctr = 0
    for i in range(Nat):
        for j in range(i,Nat):
            if (i!=j):
                val = compute_dist(geom[k],i,j)
                r_dist[k,ctr] = val[0]
                dr_dx[k,ctr,i*3+0] = val[1]
                dr_dx[k,ctr,i*3+1] = val[2]
                dr_dx[k,ctr,i*3+2] = val[3]
                dr_dx[k,ctr,j*3+0] = val[4]
                dr_dx[k,ctr,j*3+1] = val[5]
                dr_dx[k,ctr,j*3+2] = val[6]
                ctr = ctr + 1


invr = 1.0/r_dist
