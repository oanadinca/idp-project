from app.database.models import Owner, Puppy, Match

puppies = [
	{ 'id' : 1, 'name': 'Donna', 'description': 'Female, Young,  Chihuahua Golden, Joyful and Active, Los Angeles CA', 'tag': 'available'},
	{ 'id' : 2, 'name': 'Scrappy Doo', 'description': 'Male, Young, Chihuahua Golden, Purebred, Los Angeles CA', 'tag': 'available'},
	{ 'id' : 3, 'name': 'Rocco', 'description': 'Male, Mature, Staffordshire Bull Terrier, House-trained, Good with dogs, San Fransisco CA', 'tag': 'adopted'},
	{ 'id' : 4, 'name': 'Nicky', 'description': 'Female, Adult, Anatolian Shepherd, Purebred, Good with kids, San Diego CA', 'tag': 'adopted'},
	{ 'id' : 5, 'name': 'Hula', 'description': 'Female, Young, German Shepherd Dog Mix, House-trained, Los Angeles CA', 'tag': 'available'},
	{ 'id' : 6, 'name': 'Tyson', 'description': 'Female, Young, Siberian Husky, Joyful, Good with kids, Los Angeles CA', 'tag': 'adopted'},
]

owners = [
	{ 'id' : 1, 'name': 'Dan'}, 
	{ 'id' : 2, 'name' : 'Anne'}

]

matches = [
	{ 'id' : 1, 'owner_id' : 1, 'puppy_id' : 3}
]

def init_db_data():
    for owner_json in owners:
    	owner = Owner(owner_json)
    	owner.save()

    for puppy_json in puppies:
    	puppy = Puppy(puppy_json)
    	puppy.save()

    for match_json in matches:
    	match = Match(match_json)
    	match.save()
    