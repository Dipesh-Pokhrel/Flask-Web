from app import db, Puppy

# create all tht table --> Db Table 
db.create_all()

sam = Puppy('Sammy',3)
frank = Puppy('Frankie',4)

db.session.add_all([sam,frank])
db.session.commit()

print(sam.id)
print(frank.id)