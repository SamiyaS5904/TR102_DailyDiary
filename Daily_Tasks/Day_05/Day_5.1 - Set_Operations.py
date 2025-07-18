# Day 5.1 - Set Operations in Python
# Set automatically removes duplicates
followers = {'john', 'jennie', 'jim', 'jack', 'joe', 'jennie'}

# Another set of followers
fionna_followers = {'sia', 'kim', 'joe', 'jennie'}

# Perform intersection to find mutual followers
mutual_followers = followers & fionna_followers

# Display mutual followers
print("Mutual Followers:", mutual_followers)

# Iterate over the second set and print each follower
for name in fionna_followers:
    print("Fionna's Follower:", name)
