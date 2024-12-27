from .db import db

def login(login: str, passw: str):

	value = db.execute(f'''
		SELECT * FROM users 
		WHERE login='{login}' AND password='{passw}'; 
	''').fetchall()

	if value:
		return value[0]
	
	raise Exception('Unauthorized')
    
def register(login, passw):
	value = db.execute(f'''
		SELECT * FROM users 
		WHERE login='{login}'; 
	''').fetchall()
	if value:
		raise Exception("User with this login already exists")

	db.execute(f"INSERT INTO users (login, password) VALUES ('{login}', '{passw}')")
	db.commit()

if __name__ == "__main__":
	try:
		register("admin", 'admin_password')
	except:
		pass

	user = login("admin", 'admin_password')
	print(user)