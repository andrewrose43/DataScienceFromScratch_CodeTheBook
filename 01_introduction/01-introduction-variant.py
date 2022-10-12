# List of DataSciencester users - just ID number and name. (For declaring raw data, I'm just going to ctrl-C from the
# book; this isn't an interesting thing to manually copy or practice writing multiple times.)
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

# A list of tuples showing who's friends with who, by user ID.
# Hero is friends with Dunn and Sue, for example.
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Interesting stuff begins here: let's use the above data to create a dict where keys are user IDs and values are
# lists of their friends' IDs.
'''My variant: I fit the original into a single line. I've added line breaks for readability, though - remove those 
and it's one line. This is way less efficient than the multi-line version, though, because it filters all of 
friendship_pairs once per user. A fun but useless exercise.'''
friendships =\
    {user["id"]:
        list(map(
            lambda x: x[0] if x[0] != user["id"] else x[1],
            filter(lambda fp: user["id"] in fp, friendship_pairs)))
        for user in users}

'''
My variant reduces the code to one line. Easy.
'''
def number_of_friends(user):
    '''How many friends does _user_ have?'''
    return len(friendships[user["id"]])


total_connections = sum(number_of_friends(user) for user in users)
# And let's get the average number of friends per user:
avg_connections = total_connections/len(users)


'''
Variant: use sorted() instead of .sort(), just because, and do it in one line
'''
# Now let's sort the users from most to least friends...
num_friends_by_id = sorted([(user["id"], number_of_friends(user)) for user in users], key=lambda x: x[1], reverse=True)

'''Variant: function that returns a set of all friends-of-friends instead of how many mutual friends you have with 
each friend-of-a-friend. '''
def friends_of_friends(user):
    user_id = user["id"]
    return {
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id and foaf_id not in friendships[user_id]
    }


assert friends_of_friends(users[3]) == {0, 5}

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

# Let's write a function to find users with a certain interest:
'''My variant: alternate syntax; not better or worse than the original syntax. Also added type checking, just because 
it's good practice. '''
def data_scientists_who_like(target_interest: str):
    '''Find the IDs of all users who like the target interest.'''
    return [interest[0] for interest in interests if interest[1] == target_interest]

# Let's make a faster solution than the above and build an index from interests to users.
'''My variant: alternate syntax. This version does the same thing, but the original is more readable, I think, 
and thus better.'''
from collections import defaultdict
user_ids_by_interest = defaultdict(list)
for interest in interests:
    user_ids_by_interest[interest[1]].append(interest[0])

# Now the opposite.
'''My variant: alternate syntax again, same as last block.'''
interests_by_user_id = defaultdict(list)
for interest in interests:
    interests_by_user_id[interest[0]].append(interest[1])

# Now we'll find who has the most interests in common with any given user.
# We can do this by using a Counter to track appearances of other users each time they turn out to share an interest
# with the given user.
from collections import Counter
def most_common_interests_with(user):
    uid = user["id"]
    return Counter(
        other_user_id
        for interest in interests_by_user_id[uid]
        for other_user_id in user_ids_by_interest[interest]
        if other_user_id != uid
    )

# Data matching each user's salary ($) and tenure as a data scientist (years).
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# Let's look at the average salary for each tenure. This won't be useful, since all 10 tenures are different lengths.
# Keys: years. Values: list of salaries for each tenure duration.
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)
# Now the average. Keys: years. Values: average salary for each tenure duration.
avg_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

assert avg_salary_by_tenure == {
    0.7: 48000.0,
    1.9: 48000.0,
    2.5: 60000.0,
    4.2: 63000.0,
    6: 76000.0,
    6.5: 69000.0,
    7.5: 76000.0,
    8.1: 88000.0,
    8.7: 83000.0,
    10: 83000.0
}

# A more useful task is to bucket the tenures...
def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

# Then we can group together the salaries by bucket.
# Keys: tenure buckets. Values: lists of salaries for that bucket.
salaries_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salaries_by_tenure_bucket[tenure_bucket(tenure)].append(salary)

'''My variant: alternate syntax'''
avg_salary_by_tenure_bucket = {}
for bucket, salaries in salaries_by_tenure_bucket.items():
    avg_salary_by_tenure_bucket[bucket] = sum(salaries) / len(salaries)

assert avg_salary_by_tenure_bucket == {
    'between two and five': 61500.0,
    'less than two': 48000.0,
    'more than five': 79166.66666666667
}

# "predict_paid_or_unpaid" example skipped because it's just an if-elif-else block in a function

# Last exercise: let's take the "interests" data and convert to lowercase, split it into words, and count the results.
# Weird that they want to count words instead of whole interests...
interest_word_counts = Counter(word
                               for uid, interest in interests
                               for word in interest.lower().split())
