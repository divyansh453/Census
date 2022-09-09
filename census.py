#census programme
a=input("Enter host's name:")
b=input("Enter user's name:")
d=input("Enter Password:")
c=input("Enter Village:")
cd=input("Enter your district:")
dmg=c
cmg=cd
def thanks():
    print("Thankyou for using this program,if you want to use this program again then press<1> otherwise press ENTER key..")
    nh=input('')
    if nh=='1':
        print("To change Village/City press<2>and to continue with previously used database press ENTER key.. ")
        ht=input('')
        if ht=='2':
            global c
            global cmg
            c=input("Enter Village/City :")
            cd=''
            cd=input("Enter you district:")
            cmg=cd
            repeater(a,b,c,d,cd)
        else:
            repeater(a,b,c,d,cmg)
    else:
        print("BYE...")
        while 1>0:
            break
def repeater(a,b,c,d,cd):
    def main(a,b,c,d):
        import mysql.connector as dr
        global nm
        nm=dr.connect(host=a,user=b,database=c,passwd=d)
        global nr
        nr=nm.cursor()
    def reader(j):
        nr.execute(j)
        hy=nr.fetchall()
        for data in hy:
            print(data)
    def writersq(j):
        nr.execute(j)
        nm.commit()

    def district1(cd):
        dft="show tables from divyanshu"
        nr.execute(dft)
        sdf=nr.fetchall()
        L6=[]
        L7=[]
        for r in sdf:
            L6.append(r)
        l6=len(L6)
        for r1 in range(l6):
            data5=L6[r1]
            r2=data5[0]
            L7.append(r2)
        l7=len(L7)
        if l7==0:
            dft="create table divyanshu."+cd+"(Village_name varchar(50) primary key)"
            writersq(dft)
        else:
            def ret():
                m=''
                for r3 in range(l7):
                    try:
                        if str(L7[r3])==str(cd.lower()):
                            m='yes'
                    except:
                        m='no'
                return m
            mt=ret()
            if mt=='yes':
                print("")
            else:
                dft="create table divyanshu."+cd+"(Village_name varchar(50) primary key)"
                print(dft)
                writersq(dft)
                
    def district(cd):
        sde="select*from divyanshu."+cd
        nr.execute(sde)
        sdf=nr.fetchall()
        L4=[]
        L5=[]
        for r in sdf:
            L4.append(r)
        l1=len(L4)
        for r in range(l1):
            data6=L4[r]
            r3=data6[0]
            L5.append(r3)
        l5=len(L5)
        if l5==0:
            dfs="insert into divyanshu."+cd+" values('"+c+"')"
            writersq(dfs)
        else:
            def ret1():
                m=''
                for r4 in range(l5):
                    try:
                        if (L5[r4]).lower()==c.lower():
                            m='yes'
                    except:
                        m='no'
                return m
            mt=ret1()
            if mt=='yes':
                print('')
            else:
                dfs="insert into divyanshu."+cd+" values('"+c+"')"
                writersq(dfs)
    def district3():
        def district4(r10):
                global facount
                global fcount
                global mcount
                facount=0
                fcount=0
                mcount=0
                total=0
                hd='show tables from '+r10
                nr.execute(hd)
                data1=nr.fetchall()
                L10=[]
                L11=[]
                fa=[]
                f=[]
                m=[]
                for d1 in data1:
                    L10.append(d1)
                if len(L10)==0:
                    print("")
                else:
                    for d2 in L10:
                        fr=d2[0]
                        L11.append(fr)
                    for d3 in L11:
                        fa.append(d3)
                        facount=len(fa)
                        drf="select*from "+r10+'.'+d3+" where sex='F'"
                        nr.execute(drf)
                        dref=nr.fetchall()
                        for r in dref:
                            f.append(r)
                        fcount=len(f)
                        drm="select*from "+r10+'.'+d3+" where sex='M'"
                        nr.execute(drm)
                        drem=nr.fetchall()
                        for r in drem:
                            m.append(r)
                        mcount=len(m)
                        total=fcount+mcount
                return total,facount,fcount,mcount
        dfe='select*from divyanshu.'+cd
        nr.execute(dfe)
        datad=nr.fetchall()
        L8=[]
        L9=[]
        for r in datad:
            L8.append(r)
        l8=len(L8)
        for r in range(l8):
            data7=L8[r]
            r3=data7[0]
            L9.append(r3)
        l9=len(L9)
        toc=0
        faco=0
        fco=0
        mco=0
        for r10 in L9:
            #print(r10)
            to,fac,fc,mc=district4(r10)
            toc+=to
            faco+=fac
            fco+=fc
            mco+=mc
        
        print("Total number of villages in "+cd.title()+" district are:",l9)
        print("Total number of people in "+cd.title()+" district are:",toc)
        print("Total number of families in "+cd.title()+" district are:",faco)
        print("Female count of "+cd.title()+" district are:",fco)
        print("Male count of "+cd.title()+" district are:",mco)
    def jruri(f,gu):
        for h in range(1,f+1):
            print("Profile",h)
            he=input("Enter the name of member:")
            li=input("Father's name of member:")
            be=input("Age:")
            bo=input("DOB(YYYY-MM-DD):")
            gt=input("Enter Aadhar number:")
            o=input("Employed/Unemployed:")
            gy=input("Sex(M/F):")
            def aadharcheck(gt):
                if len(gt)==12:
                    ne="insert into family_no_"+str(gu)+" values("+gt+",'"+he+"','"+li+"',"+be+",'"+gy+"','"+bo+"','"+o+"')"
                    writersq(ne)
                else:
                    print("Aadhar number is invalid!!")
                    gt=""
                    print("To re-enter your aadhar number press<1> otherwise press Enter key")
                    erw=input("")
                    if erw=='1':
                        gt=input("Re-enter your Aadhar number:")
                        aadharcheck(gt)
            aadharcheck(gt)
               
        print("Now data is:")
        ert="select*from family_no_"+gu
        print("Order of data:S.no,Aadhar number,Name,Father's name,Age,Sex,DOB,Employment")
        reader(ert)
        try:
            print("Now details of "+dmg+"are:")
            counter()
        except:
            print(" ")
        thanks()
    def counter():
        global facount
        global fcount
        global mcount
        facount=0
        fcount=0
        mcount=0
        total=0
        hd='show tables'
        nr.execute(hd)
        data1=nr.fetchall()
        L1=[]
        L2=[]
        fa=[]
        f=[]
        m=[]
        for d1 in data1:
            L1.append(d1)
        for d2 in L1:
            fr=d2[0]
            L2.append(fr)
        for d3 in L2:
            fa.append(d3)
            facount=len(fa)
            drf="select*from "+d3+" where sex='F'"
            nr.execute(drf)
            dref=nr.fetchall()
            for r in dref:
                f.append(r)
            fcount=len(f)
            drm="select*from "+d3+" where sex='M'"
            nr.execute(drm)
            drem=nr.fetchall()
            for r in drem:
                m.append(r)
            mcount=len(m)
            total=fcount+mcount
        dmg=c
        print("Total number of families in "+dmg.title()+":",facount)
        print("Total number of people in "+dmg.title()+":",total)
        print("Female count of "+dmg.title()+":",fcount)
        print("Male count of "+dmg.title()+":",mcount)
    def creator(gty):
        der="create database "+gty
        writersq(der)
    def checker():
        print("Data is avaialable from Family no.",mn," to ",mj)
        er=input("Enter the family number for which you want to check data:")
        try:
            ert="select*from family_no_"+er
            print("Order of data:S.no,Aadhar number,Name,Father's name,Age,Sex,DOB,Employment")
            reader(ert)
        except:
            print("This table is not available...")
    def filler():
        print("Data is available from Family no.",mn," to ",mj)
        gu=input("Enter the Family number:")
        #try:
        f=int(input("Enter the number of Family Members for which you want to insert your data:"))
        jruri(f,gu)
          

    try:
        main(a,b,c,d)
    except:
        print("There is no database for",c)
        print("We are creating new database for you..")
        cmd='divyanshu'
        main(a,b,cmd,d)
        creator(c)
        repeater(a,b,c,d,cd)
    if nm.is_connected:
        shm=c+'('+cd+')'
        district1(cd)
        district(cd)
        print("***************************YOU ARE CONNECTED TO THE DATABASE OF",shm.upper(),"***************************")
        print('''********************************************MENU********************************************
                    1.TO CHECK DATA..
                    2.TO INSERT NEW DATA..
                    3.TO CHECK THE COUNTING..
                    4.TO INSERT MORE DATA IN OLD FAMILY TABLE..
                    5.TO CHECK DISTRICTWISE..
''')
        juyt=input("")
        L=[]
        G=[]
        j="show tables"
        nr.execute(j)
        ki=nr.fetchall()
        for r in ki:
            L.append(r)
        l=len(L)
        for hy in L:
            mi=hy[0]
            hu=mi[10:15]
            G.append(int(hu))
        try:
            global mj
            global mn
            mn=min(G)
            mj=max(G)
        except:
            mj=0
        def jruri1():
            n=int(input("Enter the number of families for which you want to enter data:"))
            for i in range(1,n+1):
                w=i+int(mj)
                print("Family no.",w)
                gt="create table family_no_"+str(w)+" (Aadhar_number bigint(12) not null primary key,_Name varchar(35) not null,Father_name varchar(35) not null,Age int,Sex varchar(2) not null,DOB date not null,Employed_OR_Unemployed varchar(10))"
                writersq(gt)
                nh=w
                w=0
                f=int(input("Enter the number of Family Members:"))
                for h in range(1,f+1):
                    print("Profile",h)
                    he=input("Enter the name of member:")
                    li=input("Father's name of member:")
                    be=input("Age:")
                    bo=input("DOB(YYYY-MM-DD):")
                    gt=input("Enter Aadhar number:")
                    o=input("Employed/Unemployed:")
                    gy=input("Sex(M/F):")
                    def aadharcheck(gt):
                        if len(gt)==12:
                            ne="insert into family_no_"+str(nh)+" values("+gt+",'"+he+"','"+li+"',"+be+",'"+gy+"','"+bo+"','"+o+"')"
                            writersq(ne)
                        else:
                            print("Aadhar number is invalid!!")
                            gt=""
                            print("To re-enter your aadhar number press<1> otherwise press Enter key")
                            erw=input("")
                            if erw=='1':
                                gt=input("Re-enter your Aadhar number:")
                                aadharcheck(gt)
                            
                    aadharcheck(gt)
                                
            try:
                print("Now details of "+dmg+"are:")
                counter()
            except:
                print(" ")
                thanks()
        if juyt=='1':
            checker()
        elif juyt=='2':
            jruri1()
        elif juyt=='3':
            counter()
        elif juyt=='4':
            filler()
        elif juyt=='5':
            district3()               

        else:
            print("INVALID ENTRY!!!!")
            counter()
        thanks()
            
    
z=2

while z>1:
    repeater(a,b,c,d,cd)
    z-=1
#end of programm

