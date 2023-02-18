#Using Python and the appropriate Python package of your choice, access https://randomuser.me/ api and list the top 100 male users
#Imports randomuser library

import randomuser

#Generates 100 male users randomly
users = randomuser.RandomUser.generate_users(100, {'gender': 'male'})

# Loop over each user and print their name
for user in users:
    print(user.get_first_name())

