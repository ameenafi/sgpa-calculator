while(1):
    try:
        sub1=int(input('enter the marks of sub1'))
        g1=0
        if (sub1 < 40):
            g1=0
        else:
            g1=int((sub1/10)+1)
        s1=int(g1)*int(4)
            
        sub2=int(input('enter the marks of sub2'))
        g2=0
        if (sub2 < 40):
            g2=0
        else:
            g2=int((sub2/10)+1)
        s2=int(g2)*int(4)
            
        sub3=int(input('enter the marks of sub3'))
        g3=0
        if (sub3 < 40):
            g3=0
        else:
            g3=int((sub3/10)+1)
        s3=int(g3)*int(4)
            
        sub4=int(input('enter the marks of sub4'))
        g4=0
        if (sub4 < 40):
            g4=0
        else:
            g4=int((sub4/10)+1)
        s4=int(g4)*int(4)
            
        sub5=int(input('enter the marks of sub5'))
        g5=0
        if (sub5 < 40):
            g5=0
        else:
            g5=int((sub5/10)+1)
        s5=int(g5)*int(3)
            
        sub6=int(input('enter the marks of sub6'))
        g6=0
        if (sub6 < 40):
            g1=0
        else:
            g6=int((sub6/10)+1)
        s6=int(g6)*int(3)
            

        lab1=int(input('enter the marks of lab1'))
        g7=0
        if (lab1 < 40):
            g7=0
        else:
            g7=int((lab1/10)+1)
        l1=int(g7)*int(2)
            
        lab2=int(input('enter the marks of lab2'))
        break
    except:
        print('wrong input')
g8=0
if (lab2 < 40):
      g8=0
else:
      g8=int((lab2/10)+1)
l2=int(g8)*int(2)

numa=(s1+s2+s3+s4+s5+s6+l1+l2)
dena=(4+4+4+4+3+3+2+2)
sgpa=(numa/dena)
print(sgpa)

percent=((sgpa-0.75)*10)
print(percent)
