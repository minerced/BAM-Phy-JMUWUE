def linear_regression(x_i, y_i):
    s_x= sum(x_i)
    s_y= sum(y_i)
    N=len(x_i)
    s_xy=0
    s_x2=0
    for i in range(len(x_i)):
        s_xy= x_i[i]*y_i[i]+s_xy
        s_x2= x_i[i]*x_i[i]+s_x2
    h_1=N*s_x2-(s_x)**2
    a=(s_x2*s_y-s_x*s_xy)/h_1
    b=(N*s_xy-s_x*s_y)/h_1
    return (a,b)