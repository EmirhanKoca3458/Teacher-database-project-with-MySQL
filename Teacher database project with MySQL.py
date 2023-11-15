import mysql.connector

conection = mysql.connector.connect(host="127.0.0.1",user = "root", password = "emrhn158",database = "şahıs")
cursor = conection.cursor()




class Edebiyat_Öğretmen():
    cursor = conection.cursor()
    
    def __init__(self,id,Name,Surname,Age,Year):
        
        if id is None:
            self.id = 0
        else:
            self.id = id
        
        self.Name = Name
        self.Surname = Surname
        self.Age = Age
        self.Year = Year
        
    
    def Öğretmen_Ekle(id,name,surname,age,years):
        sql = "INSERT INTO şahıs.edebiyat(id,name,surname,age,years) VALUES(%s,%s,%s,%s,%s)"
        values = (id,name,surname,age,years)
        cursor.execute(sql,values)
        
        try:
            conection.commit()
        except mysql.conection as err:
            print("Hatta",err)
        finally:
            conection.close()
            

            
    def Öğretmen_Sil(id):
        sql = "delete from şahıs.edebiyat where id=%s "
        values = (id,)

        cursor.execute(sql,values)
        
        
        try:
            conection.commit()
        except mysql.conection as err:
            print("Hatta",err)
        finally:
            conection.close()
            


    def Öğretmen_Düzenle(id,name,surname,age,years):
        
        sql = "Update şahıs.edebiyat Set  name = %s,surname = %s,age = %s,years = %s where id = %s " 
        values = (name,surname,age,years,id)
        
        cursor.execute(sql,values)
        try:
            conection.commit()
        except mysql.conection as err:
            print("Hatta",err)
        finally:
            conection.close()
        
        
        

        
        
    
    
    
    
    
    
    
    
class Matematik_Öğretmen():
    cursor = conection.cursor()
    
    def __init__(self,id,Name,Surname,Age,Year):
        
        if id is None:
            self.id = 0
        else:
            self.id = id
        
        self.Name = Name
        self.Surname = Surname
        self.Age = Age
        self.Year = Year
    
        
        
    
    def Öğretmen_Ekle(id,name,surname,age,years):
        sql = "INSERT INTO şahıs.matematik(id,name,surname,age,year) VALUES(%s,%s,%s,%s,%s)"
        values = (id,name,surname,age,years)
        cursor.execute(sql,values)
        
        try:
            conection.commit()
        except mysql.conection as err:
            print("Hatta",err)
        finally:
            conection.close()
            
            
    def Öğretmen_Sil(id):
        sql = "delete from şahıs.matematik where id=%s "
        values = (id,)

        cursor.execute(sql,values)
        
        
        try:
            conection.commit()
        except mysql.conection as err:
            print("Hatta",err)
        finally:
            conection.close()
            

    def Öğretmen_Düzenle(id,name,surname,age,years):
        
        sql = "Update şahıs.edebiyat Set  name = %s,surname = %s,age = %s,years = %s where id = %s " 
        values = (name,surname,age,years,id)
        
        cursor.execute(sql,values)
        try:
            conection.commit()
        except mysql.conection as err:
            print("Hatta",err)
        finally:
            conection.close()
        
    
    
    
    
    
    
class Tarih_Öğretmen():
    cursor = conection.cursor()
    
    def __init__(self,id,Name,Surname,Age,Year):
        
        if id is None:
            self.id = 0
        else:
            self.id = id
        
        self.Name = Name
        self.Surname = Surname
        self.Age = Age
        self.Year = Year
    
    
    def Öğretmen_Ekle(id,name,surname,age,years):
        sql = "INSERT INTO şahıs.tarih(id,name,surname,age,years) VALUES(%s,%s,%s,%s,%s)"
        values = (id,name,surname,age,years)
        cursor.execute(sql,values)
        
        try:
            conection.commit()
        except mysql.conection as err:
            print("Hatta",err)
        finally:
            conection.close()   


    def Öğretmen_Sil(id):
        sql = "delete from şahıs.tarih where id=%s "
        values = (id,)

        cursor.execute(sql,values)
        
        
        try:
            conection.commit()
        except mysql.conection as err:
            print("Hatta",err)
        finally:
            conection.close()
            

    def Öğretmen_Düzenle(id,name,surname,age,years):
        
        sql = "Update şahıs.edebiyat Set  name = %s,surname = %s,age = %s,years = %s where id = %s " 
        values = (name,surname,age,years,id)
        
        cursor.execute(sql,values)
        try:
            conection.commit()
        except mysql.conection as err:
            print("Hatta",err)
        finally:
            conection.close()
        
    
    
    
    
    
class Coğrafya_Öğretmen():

    cursor = conection.cursor()

    def __init__(self,id,Name,Surname,Age,Year):
        
        if id is None:
            self.id = 0
        else:
            self.id = id
        
        self.Name = Name
        self.Surname = Surname
        self.Age = Age
        self.Year = Year
    

    def Öğretmen_Ekle(id,name,surname,age,years):
        sql = "INSERT INTO şahıs.coğrafya(id,name,surname,age,years) VALUES(%s,%s,%s,%s,%s)"
        values = (id,name,surname,age,years)
        cursor.execute(sql,values)
        
        try:
            conection.commit()
        except mysql.conection as err:
            print("Hatta",err)
        finally:
            conection.close()
            
            
            
    def Öğretmen_Sil(id):
        sql = "delete from şahıs.coğrafya where id=%s "
        values = (id,)

        cursor.execute(sql,values)
        
        
        try:
            conection.commit()
        except mysql.conection as err:
            print("Hatta",err)
        finally:
            conection.close()
            
            

    def Öğretmen_Düzenle(id,name,surname,age,years):
        
        sql = "Update şahıs.edebiyat Set  name = %s,surname = %s,age = %s,years = %s where id = %s " 
        values = (name,surname,age,years,id)
        
        cursor.execute(sql,values)
        try:
            conection.commit()
        except mysql.conection as err:
            print("Hatta",err)
        finally:
            conection.close()
        
    
    


########################################################################################################################################



    
while True:
    işlem = input("Hoşgeldiniz\n1-Edebiyat Öğretmeni İşlemi\n2-Matematik Öğretmeni İşlemi\n3-Tarih Öğretmeni İşlemi\n4-Coğrafya Öğretmeni İşlemi\n5-Çıkış(5 > Basınız)\nSEÇİM: ")
    
    
    if işlem == "1":
        
    
        işlem2 = input("1-Öğretmen Ekle\n2-Öğretmen Sil\n3-Öğretmen İşlem Düzenle\nSEÇİM:")


        if işlem2 == "1":
                id= input("İd:")
                name= input("Name")
                surname=input("Surname")
                age=input("Age:")
                years=input("Years:")
                Edb=Edebiyat_Öğretmen
                Edb.Öğretmen_Ekle(id,name,surname,age,years,)
        
        
        
        elif işlem2 == "2":
            
            id = input("Silinecek Öğretmenin İD numarası nedir ?")
            Edebiyat_Öğretmen.Öğretmen_Sil(id)
            
            
        elif işlem2 == "3":
            
                id= input("İd:")
                name= input("Name")
                surname=input("Surname")
                age=input("Age:")
                years=input("Years:")
                Edebiyat_Öğretmen.Öğretmen_Düzenle(id,name,surname,age,years)
            
                
                
                
                # mat
                
    elif işlem == "2":
        
            işlem3 = input("1-Öğretmen Ekle\n2-Öğretmen Sil\n3-Öğretmen İşlem Düzenle\nSEÇİM:")
            
            if işlem3 == "1":
                id= input("İd:")
                name= input("Name")
                surname=input("Surname")
                age=input("Age:")
                years=input("Years:")
                Mth=Matematik_Öğretmen
                Mth.Öğretmen_Ekle(id,name,surname,age,years)
                
                
                
            elif işlem == "2":
                id = input("Silinecek Öğretmenin İD numarası nedir ?")
                Matematik_Öğretmen.Öğretmen_Sil(id)
            
            
            
            elif işlem == "3":
                id= input("İd:")
                name= input("Name")
                surname=input("Surname")
                age=input("Age:")
                years=input("Years:")
                Matematik_Öğretmen.Öğretmen_Düzenle(id,name,surname,age,years)
            
            
            # tarih
            
    elif işlem == "3":
        
            işlem4 = input("1-Öğretmen Ekle\n2-Öğretmen Sil\n3-Öğretmen İşlem Düzenle\nSEÇİM:")
            
            if işlem4 == "1":
                id= input("İd:")
                name= input("Name")
                surname=input("Surname")
                age=input("Age:")
                years=input("Years:")
                Trh=Tarih_Öğretmen
                Trh.Öğretmen_Ekle(id,name,surname,age,years)
                
            elif işlem == "2":
                
                id = input("Silinecek Öğretmenin İD numarası nedir ?")
                Tarih_Öğretmen.Öğretmen_Sil(id)
            
            elif işlem == "3":
                id= input("İd:")
                name= input("Name")
                surname=input("Surname")
                age=input("Age:")
                years=input("Years:")
                Tarih_Öğretmen.Öğretmen_Düzenle(id,name,surname,age,years)
            
        
                # coğ
                
    elif işlem == "4":
        
            işlem5 = input("1-Öğretmen Ekle\n2-Öğretmen Sil\n3-Öğretmen İşlem Düzenle\nSEÇİM:")
            
            if işlem5 == "1":
                id= input("İd:")
                name= input("Name")
                surname=input("Surname")
                age=input("Age:")
                years=input("Years:")
                Coğ=Coğrafya_Öğretmen
                Coğ.Öğretmen_Ekle(id,name,surname,age,years)
                
                
            elif işlem == "2":
                id = input("Silinecek Öğretmenin İD numarası nedir ?")
                Coğrafya_Öğretmen.Öğretmen_Sil(id)
            
            elif işlem == "3":
                id= input("İd:")
                name= input("Name")
                surname=input("Surname")
                age=input("Age:")
                years=input("Years:")
                Coğrafya_Öğretmen.Öğretmen_Düzenle(id,name,surname,age,years)
                
            result = input("devam etmek istiyor msunuz ?")
            if result == "E":
                continue
            elif result == "H":
                break
            conection.close()
    else:
        print("Yanlış tuş girdiniz >")


                
            

            
            

            
            
    
    
    
    


    
    

