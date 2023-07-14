import instaloader
import pandas as pd


bot = instaloader.Instaloader()
#bot.login(user="dragyaug", passwd="dr79wsim1979@gan")


profile = instaloader.Profile.from_username(bot.context, 'tapetedekor.si')
print(type(profile))

# Retrieving all posts in an object
posts = profile.get_posts()
 
# Iterating and downloading all the individual posts
for index, post in enumerate(posts, 1):
	bot.download_post(post, target=f"{profile.username}_{index}")


# Instagram Handle and Profile ID
print("Username:", profile.username)
print("User ID", profile.userid)
# Number of Followers and Followees
print("# of followers:", profile.followers)
print("# of followees", profile.followees)  