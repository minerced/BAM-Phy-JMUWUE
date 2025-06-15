def linear_regression(x_i, y_i, o):
    s_x= sum(x_i)
    s_y= sum(y_i)
    N=len(x_i)
    s_xy=0
    s_x2=0
    for i in range(len(x_i)):
        s_xy= x_i[i]*y_i[i]+s_xy
        s_x2= x_i[i]*x_i[i]+s_x2
    h1=N*s_x2-(s_x)**2
    a=(s_x2*s_y-s_x*s_xy)/h1
    o_a=(o**2)*s_x2/h1
    b=(N*s_xy-s_x*s_y)/h1
    o_b=N*(o**2)*h1
    return (a, o_a ,b, o_b)