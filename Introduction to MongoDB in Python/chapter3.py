from pprint import pprint
from pymongo import MongoClient
from operator import itemgetter
from collections import Counter


client = MongoClient()
db = client.nobel

# ex 1 "Rounding up the G.S. crew"
docs = db.laureates.find(
    filter={"firstname": {"$regex": "^G"},
            "surname": {"$regex": "^S"}},
    projection=["firstname", "surname"])

# Iterate over docs and concatenate first name and surname
full_names = [doc["firstname"] + " " + doc["surname"] for doc in docs]

# Print the full names
print(full_names)


# ex 2 "Doing our share of data validation"
# Save documents, projecting out laureates share
prizes = db.prizes.find({}, ["laureates.share"])

# Iterate over prizes
for prize in prizes:
    # Initialize total share
    total_share = 0

    # Iterate over laureates for the prize
    for laureate in prize["laureates"]:
        # add the share of the laureate to total_share
        total_share += 1 / float(laureate["share"])

    # Print the total share
    print(total_share)


# ex 3 "Sorting together: MangoDB + Python"
def all_laureates(prize):
    # sort the laureates by surname
    sorted_laureates = sorted(
        prize["laureates"], key=itemgetter("surname"))

    # extract surnames
    surnames = [laureate["surname"] for laureate in sorted_laureates]

    # concatenate surnames separated with " and "
    all_names = " and ".join(surnames)

    return all_names


# find physics prizes, project year and name, and sort by year
docs = db.prizes.find(
    filter={"category": "physics"},
    projection=["year", "laureates.firstname", "laureates.surname"],
    sort=[("year", 1)])

# print the year and laureate names (from all_laureates)
for doc in docs:
    print("{year}: {names}".format(
        year=doc["year"], names=all_laureates(doc)))


# ex 4 "Gap year"
# original categories from 1901
original_categories = db.prizes.distinct("category", {"year": "1901"})
print(original_categories)

# project year and category, and sort
docs = db.prizes.find(
    filter={},
    projection={"year": 1, "category": 1, "_id": 0},
    sort=[("year", -1), ("category", 1)]
)

# print the documents
for doc in docs:
    print(doc)


# ex 5 "Recently single?"
# Specify an index model for compound sorting
index_model = [("category", 1), ("year", -1)]
db.prizes.create_index(index_model)

# Collect the last single-laureate year for each category
report = ""
for category in sorted(db.prizes.distinct("category")):
    doc = db.prizes.find_one(
        {"category": category, "laureates.share": "1"},
        sort=[("year", -1)]
    )
    report += "{category}: {year}\n".format(**doc)

print(report)


# ex 6 "Born and affiliated"
# Ensure an index on country of birth
db.laureates.create_index([("bornCountry", 1)])

# Collect a count of laureates for each country of birth
n_born_and_affiliated = {
    country: db.laureates.count_documents({
        "bornCountry": country,
        "prizes.affiliations.country": country
    })
    for country in db.laureates.distinct("bornCountry")
}

five_most_common = Counter(n_born_and_affiliated).most_common(5)
print(five_most_common)


# ex 7 "The first five prizes with quarter shares"
# Fetch prizes with quarter-share laureate(s)
filter_ = {"laureates.share": "4"}

# Save the list of field names
projection = ["category", "year", "laureates.motivation"]

# Save a cursor to yield the first five prizes
cursor = db.prizes.find(filter_, projection).sort("year").limit(5)
pprint(list(cursor))


# ex 8 "Pages of particle-prized people"
# Write a function to retrieve a page of data

def get_particle_laureates(page_number=1, page_size=3):
    if page_number < 1 or not isinstance(page_number, int):
        raise ValueError("Pages are natural numbers (starting from 1).")
    particle_laureates = list(
        db.laureates.find(
            {"prizes.motivation": {"$regex": "particle"}},
            ["firstname", "surname", "prizes"])
        .sort([("prizes.year", 1), ("surname", 1)])
        .skip(page_size * (page_number - 1))
        .limit(page_size))
    return particle_laureates


# Collect and save the first nine pages
pages = [get_particle_laureates(page_number=page)
         for page in range(1, 9)]
pprint(pages[0])
