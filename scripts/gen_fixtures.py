import json
import random
from faker import Faker

fake = Faker("fr_FR")

APP = "app"
OUTPUT = "app/fixtures/books_1000.json"

NB_AUTHORS = 60
NB_CATEGORIES = 12
NB_BOOKS = 1200  # > 1000 comme demandé

data = []
pk = {"author": 1, "category": 1, "book": 1, "exemplar": 1}

# ================= AUTHORS =================
authors = []
for _ in range(NB_AUTHORS):
    authors.append(pk["author"])
    data.append(
        {
            "model": f"{APP}.author",
            "pk": pk["author"],
            "fields": {
                "firstname": fake.first_name(),
                "lastname": fake.last_name(),
                "birthdate": fake.date_between("-90y", "-30y").isoformat(),
                "biography": fake.text(300),
            },
        }
    )
    pk["author"] += 1

# ================= CATEGORIES =================
category_names = [
    "Roman",
    "Essai",
    "Science-fiction",
    "Fantasy",
    "Histoire",
    "Philosophie",
    "Poésie",
    "Littérature africaine",
    "Jeunesse",
    "Policier",
    "Biographie",
    "Politique",
]

categories = []
for name in category_names:
    categories.append(pk["category"])
    data.append(
        {
            "model": f"{APP}.category",
            "pk": pk["category"],
            "fields": {
                "name": name,
                "description": fake.sentence(),
            },
        }
    )
    pk["category"] += 1

# ================= BOOKS + EXEMPLARS =================
for _ in range(NB_BOOKS):
    book_pk = pk["book"]

    data.append(
        {
            "model": f"{APP}.book",
            "pk": book_pk,
            "fields": {
                "title": fake.sentence(4).replace(".", ""),
                "author": random.sample(authors, random.randint(1, 2)),
                "category": random.sample(categories, random.randint(1, 3)),
                "publication_date": fake.date_between("-70y", "today").isoformat(),
                "summary": fake.text(500),
                "isbn": fake.isbn13(),
                "cover_image": "",
            },
        }
    )
    pk["book"] += 1

    # 2 à 5 exemplaires par livre
    for _ in range(random.randint(2, 5)):
        data.append(
            {
                "model": f"{APP}.exemplar",
                "pk": pk["exemplar"],
                "fields": {
                    "book": book_pk,
                    "state": random.choice(["new", "good", "used", "damaged"]),
                    "available": random.choice([True, False]),
                    "barcode": f"BK-{book_pk}-{pk['exemplar']}",
                },
            }
        )
        pk["exemplar"] += 1

# ================= WRITE JSON =================
with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✔ Fixture générée : {OUTPUT}")
print(f"✔ Livres : {NB_BOOKS}")
