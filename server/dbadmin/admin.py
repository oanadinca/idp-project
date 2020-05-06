import sys
sys.path.append("..") # Adds higher directory to python modules path.

from app import db
from app.database.models import Puppy, Match, Owner

from sqlalchemy import literal_column
from sqlalchemy_imageattach.context import store_context

def get_puppies():
	try:
		query_result = db.session.query(Puppy).all()
	except Exception as e:
		print(e)

	for puppy in query_result:
		print(puppy.to_json)

def add_or_update_puppy(id, name, description, tag):

	my_json = {}
	my_json['id'] = id
	my_json['name'] = name
	my_json['description'] = description
	my_json['tag'] = tag

	puppy = Puppy(my_json)

	try:
		query_result = db.session.query(Puppy).filter(Puppy.id == id).all()
		query_result[0].delete()
		puppy.save()
	except Exception as e:
		puppy.save()

	response = "Successfully added or updated puppy"
	return response

def delete_puppy(id):
	try:
		query_result = db.session.query(Puppy).filter(Puppy.id == id).all()
		query_result[0].delete()
	except Exception as e:
		print("No puppy with this id: " + str(id))

	response = "Successfully deleted puppy"

	return response

def get_owners():
	try:
		query_result = db.session.query(Owner).all()
	except Exception as e:
		print(e)

	for owner in query_result:
		print(owner.to_json)

def delete_owner(id):
	try:
		query_result = db.session.query(Owner).filter(Owner.id == id).all()
		query_result[0].delete()
	except Exception as e:
		print("No owner with this id: " + str(id))

	response = "Successfully deleted owner"

def get_matches():
	try:
		query_result = db.session.query(Match).all()
	except Exception as e:
		print(e)

	for match in query_result:
		print(match.to_json)

def get_match(id):
	try:
		query_result = db.session.query(Match).filter(Match.id == id).all()
	except Exception as e:
		print(e)

	print(query_result[0].to_json)


def add_or_update_match(id, owner_id, puppy_id):

	my_json = {}
	my_json['id'] = id
	my_json['owner_id'] = owner_id
	my_json['puppy_id'] = puppy_id

	match = Match(my_json)

	try:
		query_result = db.session.query(Match).filter(Match.id == id).all()

		puppy_id_old = query_result[0].puppy_id
		puupy_result = db.session.query(Puppy).filter(Puppy.id == puppy_id_old).all()
		if puupy_result[0].tag == 'available':
			puupy_result[0].tag = 'adopted'
		else:
			puupy_result[0].tag = 'available'

		query_result[0].delete()

		puupy_result = db.session.query(Puppy).filter(Puppy.id == puppy_id).all()
		puupy_result[0].tag = 'adopted'

		match.save()
	except Exception as e:
		puupy_result = db.session.query(Puppy).filter(Puppy.id == puppy_id).all()
		puupy_result[0].tag = 'adopted'

		match.save()

	response = "Successfully added or updated match"
	return response

def delete_match(id):
	try:
		query_result = db.session.query(Match).filter(Match.id == id).all()
		
		puppy_id = query_result[0].puppy_id
		puupy_result = db.session.query(Puppy).filter(Puppy.id == puppy_id).all()
		puupy_result[0].tag = 'available'

		query_result[0].delete()
	except Exception as e:
		print("No match with this id: " + str(id))

	response = "Successfully deleted match"

	return response


adminOps = {10: get_puppies,\
			12: add_or_update_puppy,\
			13: delete_puppy,\
			20: get_owners,\
			23: delete_owner,\
			30: get_matches,\
			31: get_match,\
			32: add_or_update_match,\
			33: delete_match}



while (True):
	input_code = int(input("\nChoose op:\n"
					"10 - get all puppies\n"
					"12 - add or update puppy\n"
    				"13 - delete puppy\n"
   					"20 - get all owners\n"
    				"23 - delete owner\n"
    				"30 - get all matches\n"
    				"31 - get match\n"
  					"32 - add or update match\n"
    				"33 - delete match\n"
    				"0  - break\n"))

	if input_code == 0:
		break
	else:
		if input_code == 10 or input_code == 20 or input_code == 30:
			adminOps[input_code]()

		if input_code == 12:
			id = int(input("\nInsert puppy id:\n"))
			name = input("\nInsert puppy name:\n")
			description = input("\nInsert puppy description:\n")
			tag = input("\nInsert puppy tag:\n")
			print(adminOps[input_code](id,name,description,tag))

		if input_code == 13 or input_code == 23 or input_code == 33:
			id = int(input("\nInsert id to delete entire field:\n"))
			print(adminOps[input_code](id))

		if input_code == 31:
			id = int(input("\nInsert id to get entire field:\n"))
			print(adminOps[input_code](id))

		if input_code == 32:
			id = int(input("\nInsert match id:\n"))
			owner_id = int(input("\nInsert match owner_id:\n"))
			puppy_id = int(input("\nInsert match puppy_id:\n"))
			print(adminOps[input_code](id,owner_id,puppy_id))


