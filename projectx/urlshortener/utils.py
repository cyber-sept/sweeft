from random import choices
from string import ascii_letters, digits

from .models import Short


hash_len = 5
chars = ascii_letters + digits


# random hash generator function
def random_hash():
	hash_code =  ''.join(choices(chars, k=hash_len))

	# check if hash already exists in database
	if Short.objects.filter(short_url=hash_code).exists():
		return random_hash()

	return hash_code
