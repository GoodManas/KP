from .db import time_tracking

def login(login: str, passw: str):

	value = time_tracking.execute(f'''
		SELECT * FROM users 
		WHERE login='{login}' and password='{passw}'; 
	''').fetchall()

	if value:
		return value[0]
	
	raise Exception('Unauthorized')
    
def register(login, passw):
	value = time_tracking.execute(f'SELECT * FROM users WHERE login="{login}"; ').fetchall()
	if value:
		raise Exception("User with this login already exists")

	time_tracking.execute(f"INSERT INTO users (login, password) VALUES ('{login}') , '{passw}')")

if __name__ == "__main__":
	user = login("admin", 'admin_password')
	print(user)
	register("admin", 'admin_password')