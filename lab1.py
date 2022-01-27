class TshirtSHOP ():
    def __init__(self, ID, Name):
        self.ID = ID
        self.Name = Name
        
    def SizeS (self, SizeS ):
        self.SizeS = SizeS
        self.SizeS_Price = 280
    def SizeM (self, SizeM ):
        self.SizeM = SizeM
        self.SizeM_Price = 290
    def SizeL (self, SizeL ):
        self.SizeL = SizeL
        self.SizeL_Price = 300
    def SizeXL (self, SizeXL ):
        self.SizeXL = SizeXL
        self.SizeXL_Price = 310
    def SizeXXL (self, SizeXXL ):
        self.SizeXXL = SizeXXL
        self.SizeXXL_Price = 320
    def __str__ (self):
        return "Size S\t: {}ตัว\nSize M: {} ตัว\nSize L\t: {} ตัว\nSize XL\t: {} ตัว\nSize XXL\t: {} ตัว".format(self.SizeS, self.SizeM, self.SizeL, self.SizeXL, self.SizeXXL)

    def Total (self):
        return self.SizeS*self.SizeS_Price + self.SizeM*self.SizeM_Price + self.SizeL*self.SizeL_Price + self.SizeXL*self.SizeXL_Price + self.SizeXXL*self.SizeXXL_Price

    def paid (self, Paid):
        self.Paid = Paid

    def change (self):
        return self.Paid - self.Total() 

Member1 = TshirtSHOP("64015172", "Aekarin")
Member2 = TshirtSHOP("64015019", "Jaruphat")

Memberlist = [Member1, Member2]
while True:
    Member = str(input ("Please Enter ID : "))
    Member = [TshirtSHOP for TshirtSHOP in Memberlist if TshirtSHOP.ID == Member]
    for TshirtSHOP in Member:
        print ("สวัสดี "+TshirtSHOP.Name)
        TshirtSHOP.SizeS(0)
        TshirtSHOP.SizeM(0)
        TshirtSHOP.SizeL(0)
        TshirtSHOP.SizeXL(0)
        TshirtSHOP.SizeXXL(0)
        if TshirtSHOP in Member:
            Status =  True
            Status1 = True
            while Status:
                Need = input("ต้องการสั่งซื้อใช่หรือไม่ Y/N : ").upper()
                if Need == "Y" or "y" :
                    Status1 = True
                    while Status1:
                        print("เลือกไซซ์เสื้อที่ต้องการ \n1).Size S 280บ.\n2).Size M 290บ.\n3).Size L 300บ.\n4).Size XL 310บ.\n5).Size XXL320บ.")
                        print("ออกจากระบบหรือเช็คบิลให้พิมพ์ N")
                        Tshirt = input("ใส่ไซซ์เสื้อที่ต้องการ: ")
                        if Tshirt == "1" :
                            TshirtSHOP.SizeS = int(input("ต้องการซื้อกี่ตัว : "))
                        elif Tshirt == "2" : 
                            TshirtSHOP.SizeM = int(input("ต้องการซื้อกี่ตัว : "))
                        elif Tshirt == "3" :
                            TshirtSHOP.SizeL = int(input("ต้องการซื้อกี่ตัว : "))
                        elif Tshirt == "4" :
                            TshirtSHOP.SizeXL = int(input("ต้องการซื้อกี่ตัว : "))
                        elif Tshirt == "5" :
                            TshirtSHOP.SizeXXL = int(input("ต้องการซื้อกี่ตัว : "))
                        elif Tshirt == "N" or "n" :
                            Status1 = False  
                    print(TshirtSHOP.__str__())
                    print("ราคารวม ")
                    print(TshirtSHOP.Total())
                    print("บาท")
                    if TshirtSHOP.Total() > 0 :
                        TshirtSHOP.Paid = int(input("จ่ายเงินเป็นจำนวน : "))
                        if  TshirtSHOP.change() > 0 :    
                            print("เงินทอน = "+str(TshirtSHOP.change()))
                        else :
                            print ("ขอบคุณที่ใช้บริการ")
                        break
                else :
                    print ("See you again.")
                    break
    if TshirtSHOP not in Member :
        print("กรุณากรอกใหม่อีกครั้ง")
