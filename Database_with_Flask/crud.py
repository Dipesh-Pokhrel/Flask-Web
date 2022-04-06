from app import db, Puppy

# Create 
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

# READ : ORM object
all_puppies = Puppy.query.all()  # list of all puppies objects in the table.
print(all_puppies)

# READ Puppy by id
puppy_one = Puppy.query.get(1)
print(puppy_one)

# Filter by name : produce some sql code for us
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())
#['Frankie is 3 years old']

# UPDATE
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

# Delete
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()

# Check database
all_puppies = Puppy.query.all()
print(all_puppies)