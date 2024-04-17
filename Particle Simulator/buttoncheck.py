def check(color1,color2,rect,x,y,on):
    if on:
        return color1
    elif rect[0] <= x <= rect[0]+rect[2] and rect[1] <= y <= rect[3] <= y:
        return color1
    else:
        return color2
