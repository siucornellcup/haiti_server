"""
Bulk loads data into the database.
Functions provided for bulk loading doctors, patients, and nurses tables.
Functions provided for clearing all rows from doctors, patients and nurses tables.

Lots of repetition in this script as there is no easy way to pass table and field names as parameters

Don't forget to conn.close() and cur.close()
"""

from faker import Factory
import psycopg2
gender = ['Male','Female']
#These ethnicities are taken from the US Census.
ethnicity = ['White','Black','American Indian',
			 'Asian Indian','Chinese','Filipino',
			 'Other Asian','Japanese','Korean',
			 'Vietnamese','Native Hawaiian','Guamanian',
			 'Samoan','Other Pacific Islander','Other']
fake = Factory.create()

num_records = 1000
id_photo = open("test_img.jpg","rb").read()

def dblogin():
	conn = psycopg2.connect("dbname=postgres user=postgres password=hi host=localhost")
	cur = conn.cursor()
	return conn, cur

def load_patients(num_records):
	insertions = 0
	while insertions < num_records:
		name = fake.name()
		village = fake.city()
		dob = fake.date(pattern="%Y-%m-%d")
		gend = fake.random_element(gender)
		ethn = fake.random_element(ethnicity)
		fp_hash = fake.md5(raw_output=False)
		cur.execute("""INSERT INTO clinic.patients(name, village, dob, gender,
		 ethnicity, fingerprint_hash, id_photo) VALUES (%s, %s, %s, %s, %s, %s, %s)""", 
												    (name,
												     village, 
												     dob,
												     gend,
												     ethn,
												     fp_hash,
												     psycopg2.Binary(id_photo)))
		print "Status: " + cur.statusmessage
		conn.commit()
		insertions += 1
		print "Inserted %s into the database\n"%name

def load_nurses(num_records):
	conn, cur = dblogin()
	insertions = 0
	while insertions < num_records:
		name = fake.name()
		village = fake.city()
		dob = fake.date(pattern="%Y-%m-%d")
		gend = fake.random_element(gender)
		fp_hash = fake.md5(raw_output=False)
		cur.execute("""INSERT INTO clinic.nurses(name, village, dob, gender, 
			fingerprint_hash, id_photo) VALUES (%s, %s, %s, %s, %s, %s)""", 
												    (name,
												     village, 
												     dob,
												     gend,
												     fp_hash,
												     psycopg2.Binary(id_photo)))
		print "Status: " + cur.statusmessage
		conn.commit()
		insertions += 1
		print "Inserted %s into the database\n"%name
		

def load_doctors(num_records):
	insertions = 0
	while insertions < num_records:
		name = fake.name()
		doc_id = fake.md5(raw_output=False)
		cur.execute("INSERT INTO clinic.doctors(name, doc_id) VALUES (%s, %s)", 
												    (name,
												     doc_id,))
		print "Status: " + cur.statusmessage
		conn.commit()
		insertions += 1
		print "Inserted %s into the database\n"%name

def clear_doctors(conn,cur):
	cur.execute("DELETE FROM clinic.doctors")
	conn.commit()

def clear_patients(conn,cur):
	cur.execute("DELETE FROM clinic.patients")
	conn.commit()

def clear_nurses(conn,cur):
	cur.execute("DELETE FROM clinic.nurses")
	conn.commit()

def nurse_lookup_fp(fingerprint):
	conn, cur = dblogin()
	cur.execute("SELECT * FROM clinic.nurses WHERE fingerprint_hash = %s",(fingerprint,))
	result = cur.fetchone()
	colnames = [description[0] for description in cur.description]
	cur.close()
	conn.close()
	if result != None:
		result = zip(colnames,result)
		dict_record = {}
		for colname, value in result:
			dict_record[colname] = value
		return dict_record
	else:
		return None

#Dummy fingerprint: 00372a6fb1a467b54992df4daf0dfa49