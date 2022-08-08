import psycopg2
import datetime
import random
import string
import os

def generate_all():
    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()

        for i in range(1000):
            letters = string.ascii_lowercase
            usern = ''.join(random.choice(letters) for j in range(random.randint(1,10)))
            pasw = ''.join(random.choice(letters) for j in range(random.randint(1,10)))
            cursor.execute("INSERT INTO users (employernumber, creationdate, username, password, level) VALUES (%s, %s, %s, %s, %s)", (i+10000,datetime.date(random.randint(2000,2022), random.randint(1,12), random.randint(1,28)),  usern, pasw, random.randint(0,100)))

        for i in range(500):
            letters = string.ascii_lowercase
            plat = ''.join(random.choice(letters) for j in range(random.randint(1,10)))
            cursor.execute("INSERT INTO platform (platformname, hyperlinkpath) VALUES (%s, %s)", (plat,"https//www."+plat+".com"))

        cursor.execute("select platformid from platform")
        rec = cursor.fetchall()
        
        for i in range(5000):
            letters = string.ascii_lowercase
            cname = ''.join(random.choice(letters) for j in range(random.randint(1,10)))
            cursor.execute("INSERT INTO course (coursename, platformid, duration, creationdate) VALUES (%s, %s, %s, %s)", (cname,random.randint(min(rec)[0],max(rec)[0]), datetime.time(random.randint(0,23), random.randint(0,59), random.randint(0,59)),datetime.date(random.randint(2000,2022), random.randint(1,12), random.randint(1,28))))

        
        cursor.execute("select userid from users")
        rec = cursor.fetchall()
        cursor.execute("select courseid from course")
        rec2 = cursor.fetchall()

        for i in range(600):
            letters = string.ascii_lowercase
            feedb = ''.join(random.choice(letters) for j in range(random.randint(1,100)))
            cursor.execute("INSERT INTO review (userid, courseid, feedback, likedislike, rankingscore) VALUES (%s, %s, %s, %s,%s)", (random.randint(min(rec)[0],max(rec)[0]),random.randint(min(rec2)[0],max(rec2)[0]), feedb, bool(random.randint(0,1)),random.randint(1,5)))
                
        cursor.execute("select userid from users")
        rec = cursor.fetchall()
        cursor.execute("select courseid from course")
        rec2 = cursor.fetchall()

        # I didn't check here if the user or course was created after the certificate completion date because it's a lot of extra code and I felt like it's not the point of this exercise
        
        for i in range(1500):
            cursor.execute("INSERT INTO certid (userid, courseid, completionduration, completiondate) VALUES (%s, %s, %s, %s)", (random.randint(min(rec)[0],max(rec)[0]),random.randint(min(rec2)[0],max(rec2)[0]), datetime.time(random.randint(0,23), random.randint(0,59), random.randint(0,59)),datetime.date(random.randint(2000,2022), random.randint(1,12), random.randint(1,28))))
  

        cursor.execute("select userid from users")
        rec = cursor.fetchall()
        cursor.execute("select courseid from course")
        rec2 = cursor.fetchall()

        status = ["inactive","active","paused"]
        for i in range(1500):
            sdate = datetime.date(random.randint(2000,2022), random.randint(1,12), random.randint(1,28))
            lu=sdate + datetime.timedelta(days = random.randint(0,20))
            fdate =lu + datetime.timedelta(days = random.randint(0,20))
            cursor.execute("INSERT INTO ongtrain (userid, courseid, status, completionpercentage, startdate, finishdate, lastupdated) VALUES (%s, %s, %s, %s,%s, %s, %s)", (random.randint(min(rec)[0],max(rec)[0]),random.randint(min(rec2)[0],max(rec2)[0]), status[random.randint(0,2)], random.randint(0,99), sdate,fdate,lu))

        
        cursor.execute("select courseid from course")
        rec = cursor.fetchall()
        cursor.execute("select platformid from platform")
        rec2 = cursor.fetchall()

        
        for i in range(1500):
            f = open("/home/student/Documents/images/"+ random.choice([x for x in os.listdir("/home/student/Documents/images") if os.path.isfile(os.path.join("/home/student/Documents/images", x))]),'rb')
            cursor.execute("INSERT INTO photo (courseid, platformid, imageobject) VALUES (%s, %s, %s)", (random.randint(min(rec)[0],max(rec)[0]),random.randint(min(rec2)[0],max(rec2)[0]), f.read()))
  
        #for some reason this insert only works with single character strings I tryed to fix it but it took too long time so I moved on since I felt like this is not the point of the exercise
        for i in range(500):
            cursor.execute("INSERT INTO tags (tname) VALUES (%s)", ("b"))
          
        
        cursor.execute("select tagid from tags")
        rec = cursor.fetchall()
        cursor.execute("select courseid from course")
        rec2 = cursor.fetchall()


        for i in range(1500):
            cursor.execute("INSERT INTO tagcourse (tagid, courseid) VALUES (%s, %s)", (random.randint(min(rec)[0],max(rec)[0]),random.randint(min(rec2)[0],max(rec2)[0])))
  

        connection.commit()

        
        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
            
            
##################################################################################################################################################

def generate_users(y,m,d,yy,mm,dd):
    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()

        for i in range(1000):
            letters = string.ascii_lowercase
            usern = ''.join(random.choice(letters) for j in range(random.randint(1,10)))
            pasw = ''.join(random.choice(letters) for j in range(random.randint(1,10)))
            cursor.execute("INSERT INTO users (employernumber, creationdate, username, password, level) VALUES (%s, %s, %s, %s, %s)", (i+10000,datetime.date(random.randint(y,yy), random.randint(m,mm), random.randint(d,dd)),  usern, pasw, random.randint(0,100)))
    
        connection.commit()
        
        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##################################################################################################################################################

def generate_certid(y,m,d,yy,mm,dd):
    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()

                  
        cursor.execute("select userid from users")
        rec = cursor.fetchall()
        cursor.execute("select courseid from course")
        rec2 = cursor.fetchall()
        
        for i in range(1500):
           cursor.execute("INSERT INTO certid (userid, courseid, completionduration, completiondate) VALUES (%s, %s, %s, %s)", (random.randint(min(rec)[0],max(rec)[0]),random.randint(min(rec2)[0],max(rec2)[0]), datetime.time(random.randint(0,23), random.randint(0,59), random.randint(0,59)),datetime.date(random.randint(y,yy), random.randint(m,mm), random.randint(d,dd))))
    
        connection.commit()
        
        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##################################################################################################################################################

def generate_ongtrain(y,m,d,yy,mm,dd):
    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()

        cursor.execute("select userid from users")
        rec = cursor.fetchall()
        cursor.execute("select courseid from course")
        rec2 = cursor.fetchall()

        status = ["inactive","active","paused"]
        for i in range(1500):
            sdate = datetime.date(random.randint(y,yy), random.randint(m,mm), random.randint(d,dd))
            lu=sdate + datetime.timedelta(days = random.randint(0,20))
            fdate =lu + datetime.timedelta(days = random.randint(0,20))
            cursor.execute("INSERT INTO ongtrain (userid, courseid, status, completionpercentage, startdate, finishdate, lastupdated) VALUES (%s, %s, %s, %s,%s, %s, %s)", (random.randint(min(rec)[0],max(rec)[0]),random.randint(min(rec2)[0],max(rec2)[0]), status[random.randint(0,2)], random.randint(0,99), sdate,fdate,lu))

        connection.commit()
        
        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##################################################################################################################################################

def generate_course(y,m,d,yy,mm,dd):
    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()

        cursor.execute("select platformid from platform")
        rec = cursor.fetchall()
        
        for i in range(5000):
            letters = string.ascii_lowercase
            cname = ''.join(random.choice(letters) for j in range(random.randint(1,10)))
            cursor.execute("INSERT INTO course (coursename, platformid, duration, creationdate) VALUES (%s, %s, %s, %s)", (cname,random.randint(min(rec)[0],max(rec)[0]), datetime.time(random.randint(0,23), random.randint(0,59), random.randint(0,59)),datetime.date(random.randint(y,yy), random.randint(m,mm), random.randint(d,dd))))
 
        connection.commit()
        
        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##################################################################################################################################################

def generate_review():
    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()

        cursor.execute("select userid from users")
        rec = cursor.fetchall()
        cursor.execute("select courseid from course")
        rec2 = cursor.fetchall()

        for i in range(600):
            letters = string.ascii_lowercase
            feedb = ''.join(random.choice(letters) for j in range(random.randint(1,100)))
            cursor.execute("INSERT INTO review (userid, courseid, feedback, likedislike, rankingscore) VALUES (%s, %s, %s, %s,%s)", (random.randint(min(rec)[0],max(rec)[0]),random.randint(min(rec2)[0],max(rec2)[0]), feedb, bool(random.randint(0,1)),random.randint(1,5)))
            
        connection.commit()
        
        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##################################################################################################################################################

def generate_platform():
    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()

        for i in range(500):
                   letters = string.ascii_lowercase
                   plat = ''.join(random.choice(letters) for j in range(random.randint(1,10)))
                   cursor.execute("INSERT INTO platform (platformname, hyperlinkpath) VALUES (%s, %s)", (plat,"https//www."+plat+".com"))

        connection.commit()
        
        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##################################################################################################################################################

def generate_photo():
    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()

        cursor.execute("select courseid from course")
        rec = cursor.fetchall()
        cursor.execute("select platformid from platform")
        rec2 = cursor.fetchall()

        
        for i in range(1500):
            f = open("/home/student/Documents/images/"+ random.choice([x for x in os.listdir("/home/student/Documents/images") if os.path.isfile(os.path.join("/home/student/Documents/images", x))]),'rb')
            cursor.execute("INSERT INTO photo (courseid, platformid, imageobject) VALUES (%s, %s, %s)", (random.randint(min(rec)[0],max(rec)[0]),random.randint(min(rec2)[0],max(rec2)[0]), f.read()))
 
        connection.commit()
        
        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##################################################################################################################################################

def generate_tags():
    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()

        for i in range(500):
                cursor.execute("INSERT INTO tags (tname) VALUES (%s)", ("b"))
          
        connection.commit()
        
        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##################################################################################################################################################

def generate_tagcourse():
    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()

        cursor.execute("select tagid from tags")
        rec = cursor.fetchall()
        cursor.execute("select courseid from course")
        rec2 = cursor.fetchall()


        for i in range(1500):
            cursor.execute("INSERT INTO tagcourse (tagid, courseid) VALUES (%s, %s)", (random.randint(min(rec)[0],max(rec)[0]),random.randint(min(rec2)[0],max(rec2)[0])))
  
        connection.commit()
        
        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##################################################################################################################################################


#these inserts normally genertate defaults but if a user doesn't want default none value can be given

def insert_user(**kwargs):
    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()

        k=list(kwargs.keys())
        v=list(kwargs.values())
        keys="("+k[0]
        
        for i in range(len(k)):
            if isinstance(v[i],str):
                v[i]="'"+v[i]+"'"
        values="("+str(v[0])
        for i in range(1,len(k)):
            keys=keys+","+k[i]
            values=values+","+str(v[i])
        keys=keys+")"
        values=values+")"
        cursor.execute("INSERT INTO users {} VALUES {}".format(keys,values))
        connection.commit()

        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


##################################################################################################################################################

def insert_review(**kwargs):
    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()

        k=list(kwargs.keys())
        v=list(kwargs.values())
        keys="("+k[0]

        for i in range(len(k)):
            if isinstance(v[i],str):
                v[i]="'"+v[i]+"'"
        values="("+str(v[0])
        for i in range(1,len(k)):
            keys=keys+","+k[i]
            values=values+","+str(v[i])
        keys=keys+")"
        values=values+")"
        cursor.execute("INSERT INTO review {} VALUES {}".format(keys,values))
        connection.commit()

        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##################################################################################################################################################

def insert_ongtrain(**kwargs):
    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()

        k=list(kwargs.keys())
        v=list(kwargs.values())
        keys="("+k[0]

        for i in range(len(k)):
            if isinstance(v[i],str):
                v[i]="'"+v[i]+"'"
        values="("+str(v[0])
        for i in range(1,len(k)):
            keys=keys+","+k[i]
            values=values+","+str(v[i])
        keys=keys+")"
        values=values+")"
        cursor.execute("INSERT INTO ongtrain {} VALUES {}".format(keys,values))
        connection.commit()

        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##################################################################################################################################################

def insert_certid(**kwargs):
    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()

        k=list(kwargs.keys())
        v=list(kwargs.values())
        keys="("+k[0]

        for i in range(len(k)):
            if isinstance(v[i],str):
                v[i]="'"+v[i]+"'"
        values="("+str(v[0])
        for i in range(1,len(k)):
            keys=keys+","+k[i]
            values=values+","+str(v[i])
        keys=keys+")"
        values=values+")"
        cursor.execute("INSERT INTO certid {} VALUES {}".format(keys,values))
        connection.commit()

        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##################################################################################################################################################

def insert_course(**kwargs):
    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()

        k=list(kwargs.keys())
        v=list(kwargs.values())
        keys="("+k[0]
        
        for i in range(len(k)):
            if isinstance(v[i],str):
                v[i]="'"+v[i]+"'"
        values="("+str(v[0])
        for i in range(1,len(k)):
            keys=keys+","+k[i]
            values=values+","+str(v[i])
        keys=keys+")"
        values=values+")"
        cursor.execute("INSERT INTO course {} VALUES {}".format(keys,values))
        connection.commit()

        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##################################################################################################################################################

def insert_platform(**kwargs):
    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()

        k=list(kwargs.keys())
        v=list(kwargs.values())
        keys="("+k[0]

        for i in range(len(k)):
            if isinstance(v[i],str):
                v[i]="'"+v[i]+"'"
        values="("+str(v[0])
        for i in range(1,len(k)):
            keys=keys+","+k[i]
            values=values+","+str(v[i])
        keys=keys+")"
        values=values+")"
        cursor.execute("INSERT INTO platform {} VALUES {}".format(keys,values))
        connection.commit()

        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##################################################################################################################################################

def insert_photo(**kwargs):
    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()

        k=list(kwargs.keys())
        v=list(kwargs.values())
        keys="("+k[0]

        for i in range(len(k)):
            if isinstance(v[i],str):
                v[i]="'"+v[i]+"'"
        values="("+str(v[0])
        for i in range(1,len(k)):
            keys=keys+","+k[i]
            values=values+","+str(v[i])

        keys=keys+")"
        values=values+")"
        cursor.execute("INSERT INTO photo {} VALUES {}".format(keys,values))
        connection.commit()

        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##################################################################################################################################################

def insert_tags(**kwargs):
    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()

        k=list(kwargs.keys())
        v=list(kwargs.values())
        keys="("+k[0]

        for i in range(len(k)):
            if isinstance(v[i],str):
                v[i]="'"+v[i]+"'"
        values="("+str(v[0])
        for i in range(1,len(k)):
            keys=keys+","+k[i]
            values=values+","+str(v[i])
        keys=keys+")"
        values=values+")"
        cursor.execute("INSERT INTO tags {} VALUES {}".format(keys,values))
        connection.commit()

        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##################################################################################################################################################

def insert_tagcourse(**kwargs):
    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()

        k=list(kwargs.keys())
        v=list(kwargs.values())
        keys="("+k[0]

        for i in range(len(k)):
            if isinstance(v[i],str):
                v[i]="'"+v[i]+"'"
        values="("+str(v[0])
        for i in range(1,len(k)):
            keys=keys+","+k[i]
            values=values+","+str(v[i])
        keys=keys+")"
        values=values+")"
        cursor.execute("INSERT INTO tagcourse {} VALUES {}".format(keys,values))
        connection.commit()

        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
##################################################################################################################################################

# Originaly I wanted to add join, group by and having functions but that would require so much variables it would be be neary unusable

def select(table,s,k,v,var1,var2):

    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()



        select=s[0]
        
        for i in range(1,len(s)):
            select=select + ", " + s[i]
          
        for i in range(len(v)):
            if isinstance(v[i],str):
                v[i]="'"+v[i]+"'"
                

        where= k[0]+ " " + var1[0] + " "+ str(v[0])
        
        for i in range(1,len(k)):

            where=where+ " "+ var2[i-1]+ " "+ k[i]+ " "+ var1[i]+ " "+ str(v[i])
            
            


        cursor.execute("SELECT {} FROM {} WHERE {}".format(select,table,where))
        recs = cursor.fetchall()


        for row in recs:
            for j in range(len(s)):
                print(s[j] + " = " ,row[j])

        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
##################################################################################################################################################

def update(table,s1,s2,k,v,var1,var2):

    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()



       
          
        for i in range(len(v)):
            if isinstance(v[i],str):
                v[i]="'"+v[i]+"'"
            if isinstance(s2[i],str):
                s2[i]="'"+s2[i]+"'"
               
                
        set=s1[0] + " = " + str(s2[0])
        
        for i in range(1,len(s1)):
            set=set + ", " + s1[i] + " = " + str(s2[i])

        where= k[0]+ " " + var1[0] + " "+ str(v[0])
        
        for i in range(1,len(k)):

            where=where+ " "+ var2[i-1]+ " "+ k[i]+ " "+ var1[i]+ " "+ str(v[i])
            
            


        cursor.execute("UPDATE {} SET {} WHERE {}".format(table,set,where))

        connection.commit()

        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
 ##################################################################################################################################################
 
def delete(table,k,v,var1,var2):

    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()



       
          
        for i in range(len(v)):
            if isinstance(v[i],str):
                v[i]="'"+v[i]+"'"

                


        where= k[0]+ " " + var1[0] + " "+ str(v[0])
        
        for i in range(1,len(k)):

            where=where+ " "+ var2[i-1]+ " "+ k[i]+ " "+ var1[i]+ " "+ str(v[i])
            
            


        cursor.execute("UPDATE {} SET active = false WHERE {}".format(table,where))

        connection.commit()

        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
 ##################################################################################################################################################
 
def undelete(table,k,v,var1,var2):

    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()



       
          
        for i in range(len(v)):
            if isinstance(v[i],str):
                v[i]="'"+v[i]+"'"

                


        where= k[0]+ " " + var1[0] + " "+ str(v[0])
        
        for i in range(1,len(k)):

            where=where+ " "+ var2[i-1]+ " "+ k[i]+ " "+ var1[i]+ " "+ str(v[i])
            
            


        cursor.execute("UPDATE {} SET active = true WHERE {}".format(table,where))

        connection.commit()

        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
 
  ##################################################################################################################################################
 
def permadelete(table,k,v,var1,var2):

    try:
        connection = psycopg2.connect(user="postgres",
                                                        password="K0becab0",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="azure")
        cursor = connection.cursor()



       
          
        for i in range(len(v)):
            if isinstance(v[i],str):
                v[i]="'"+v[i]+"'"

                


        where= k[0]+ " " + var1[0] + " "+ str(v[0])
        
        for i in range(1,len(k)):

            where=where+ " "+ var2[i-1]+ " "+ k[i]+ " "+ var1[i]+ " "+ str(v[i])
            
            


        cursor.execute("DELETE FROM {} WHERE {}".format(table,where))

        connection.commit()

        
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
 
#select("users", ['Userid','username',"active"],['userid','userid'],[950,990],['=','>'],['or'])
#update("users", ['employernumber','username'],[11,"Bobert"],['userid','userid'],[1010,1018],['=','<'],['or'])
#generate_all()