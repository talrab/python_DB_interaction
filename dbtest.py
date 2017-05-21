import sqlite3

def Main():
	try:
		con = sqlite3.connect('test.db')
		
		cur = con.cursor()
		# checking whether a 'Pets' table already exists
		cur.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="Pets"')
		data = cur.fetchone()
		if data == None:
			# It means that there is no Pets table, so lets create one
			cur.execute('CREATE TABLE Pets(Id INT, Name TEXT, Price INT)')
			cur.execute('INSERT INTO Pets VALUES(1, "Cat", 400)')
			cur.execute('INSERT INTO Pets VALUES(2, "Dog", 600)')
			cur.execute('INSERT INTO Pets VALUES(3, "Rabbit", 200)')
			cur.execute('INSERT INTO Pets VALUES(4, "Bird", 60)')
		
			con.commit()

		cur.execute('SELECT * FROM Pets')
		data = cur.fetchall()
		
		for row in data:
			print(row)

	except sqlite3.Error as e:
		if con:
			print("Error! Rolling back")
			print(e.args[0])
			con.rollback()
	finally:
		if con:
			con.close()

if __name__ == '__main__':
	Main()

