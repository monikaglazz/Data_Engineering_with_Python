from pymongo import MongoClient
from bson.regex import Regex

client = MongoClient()
db = client.nobel

# ex 1 "Never from there, but sometimes there at last"
# Countries recorded as countries of death but not as countries of birth
countries = set(db.laureates.distinct('diedCountry')) - \
    set(db.laureates.distinct('bornCountry'))
print(countries)


# ex 2 "Countries of affiliation"
# The number of distinct countries of laureate affiliation for prizes
count = len(db.laureates.distinct('prizes.affiliations.country'))
print(count)


# ex 3 "Triple plays (mostly) all around"
# Save a filter for prize documents with three or more laureates
criteria = {"laureates.2": {"$exists": True}}

# Save the set of distinct prize categories in documents satisfying the
# criteria
triple_play_categories = set(db.prizes.distinct("category", criteria))
assert set(db.prizes.distinct("category")) - \
    triple_play_categories == {"literature"}


# ex 4 "Meanwhile, in other categories..."
# Save a filter for laureates with unshared prizes
unshared = {
    "prizes": {"$elemMatch": {
        "category": {"$nin": ["physics", "chemistry", "medicine"]},
        "share": "1",
        "year": {"$gte": "1945"},
    }}}

# Save a filter for laureates with shared prizes
shared = {
    "prizes": {"$elemMatch": {
        "category": {"$nin": ["physics", "chemistry", "medicine"]},
        "share": {"$ne": "1"},
        "year": {"$gte": "1945"},
    }}}

ratio = db.laureates.count_documents(
    unshared) / db.laureates.count_documents(shared)
print(ratio)


# ex 5 "Organizations and prizes over time"
# Save a filter for organization laureates with prizes won before 1945
before = {
    "gender": "org",
    "prizes.year": {"$lt": "1945"},
}

# Save a filter for organization laureates with prizes won in or after 1945
in_or_after = {
    "gender": "org",
    "prizes.year": {"$gte": "1945"},
}

n_before = db.laureates.count_documents(before)
n_in_or_after = db.laureates.count_documents(in_or_after)
ratio = n_in_or_after / (n_in_or_after + n_before)
print(ratio)


# ex 6 "Germany, then and now"
# Filter for laureates with "Germany" in their "bornCountry" value
criteria = {"bornCountry": Regex("Germany")}
print(set(db.laureates.distinct("bornCountry", criteria)))

# Filter for laureates with a "bornCountry" value starting with "Germany"
criteria = {"bornCountry": Regex("^Germany")}
print(set(db.laureates.distinct("bornCountry", criteria)))

# Fill in a string value to be sandwiched between the strings "^Germany "
# and "now"
criteria = {"bornCountry": Regex("^Germany " + "\\(" + "now")}
print(set(db.laureates.distinct("bornCountry", criteria)))

# Filter for currently-Germany countries of birth. Fill in a string value to
# be sandwiched between the strings "now" and "$"
criteria = {"bornCountry": Regex("now" + " Germany\\)" + "$")}
print(set(db.laureates.distinct("bornCountry", criteria)))


# ex 7 "The prized transistor"
# Save a filter for laureates with prize motivation values containing
# "transistor" as a substring
criteria = {"prizes.motivation": Regex("transistor")}

# Save the field names corresponding to a laureate's first name and last name
first, last = "firstname", "surname"
print([(laureate[first], laureate[last])
      for laureate in db.laureates.find(criteria)])
