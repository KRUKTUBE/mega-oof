pas=input("Введите пароль:  ")

def passwrda(pas):
    for i in pas:
        if i>="a" and i<= "z":
            return "буква строчная"
def passwrdA(pas):
    for i in pas:
        if i>= "A" and i <= "Z":
            return "буква заглавная"
def passwrd1(pas):
    for i in pas:
        if i>= "0" and i<= "9":
            return "буква... А стоп! Это цифра!"
            
print(passwrda(pas))
print(passwrdA(pas))
print(passwrd1(pas))
    
        
    

    