import sqlite3

def login(login, passw, signal):
    con = sqlite3.connect('handler/time_tracking')
    cur = con.cursor()
    
    #Проверка users
    cur.execute(f'SELECT * FROM users WHERE Login="{login}"; ')
    value = cur.fetchall()
    
    if value != [] and value [0][2] == passw:
        signal.emit('Успешная авторизация')
    else: 
        signal.emit('Проверьте правильность ввода')

    cur.close()
    con.close()
    
def register(login, passw, signal):
    con = sqlite3.connect('handler/time_tracking')
    cur = con.cursor()     
    
    cur.execute(f'SELECT * FROM users WHERE Login="{login}"; ')
    value = cur.fetchall()
    
    if value != []:
        signal.emit('Таокй ник уже используется')
        
    elif value == []:
        
        cur.execute(f"INSERT INTO users (login, password) VALUES ('{login}') , '{passw}')")
        signal.emit('вы успешно Зарегистрировались')
        con.commit()      

    cur.close()
    con.close() 