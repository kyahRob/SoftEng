import sqlite3

class dataLogic_Acc:
	def __init__(self):
		self.connection = sqlite3.connect("dataBase.db")
		self.cursor = self.connection.cursor()
		self.connection.row_factory = sqlite3.Row
		self.userTemp = None

	def doExist(self,user):
		self.cursor.execute("SELECT * FROM accountsP ")
		rows = self.cursor.fetchall()
		for row in rows:
			if (str(row[0]) == user):
				self.userTemp = row[0]
				self.connection.commit()
				return True
		self.connection.commit()
		return False

	def doMatch(self, pw):
		self.cursor.execute("SELECT * FROM accountsP ")
		rows = self.cursor.fetchall()
		mess = "Incorrect Password"
		for row in rows:
			if (str(row[0]) == self.userTemp):
				if(str(row[1] == pw)):
					self.connection.commit()
					return str(row[2])
				else:
					self.connection.commit()
					return mess
	def insertData(self,user,pw,fn):
		self.cursor.execute('Insert INTO accountsP(USERNAME,PASSWORD,FULLNAME) VALUES(?,?,?)',(user,pw,fn))
		self.connection.commit()