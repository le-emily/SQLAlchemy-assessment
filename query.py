"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# > It's a query object.



# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# > An association table exists when there is no clear middle connection between two tables. 
# The association table is just the "glue" that holds these tables together and doens't
# hold any values. The naming convention for this table is to combine the name of the two 
# tables you want to connect. It's a many to one relationship.


# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.get("ram")

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = Model.query.filter_by(name='Corvette', brand_id='che').all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = (Brand.query.filter(Brand.founded == 1903,
                         Brand.discontinued.is_(None)).all())

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = (Brand.query.filter(db.or_(Brand.discontinued.isnot(None),
                                Brand.founded < 1950)).all())

# Get all models whose brand_id is not ``for``.
q8 = Model.query.filter(Model.brand_id != 'for').all()


# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    # write a query to get the year of all models
    models = Model.query.filter_by(year=year).all()

    if models:
        for model in models:
            print "{} {} {}".format(model.brand.name, model.name, model.brand.headquarters)
    else:
        print "Nothing in this database!"


def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    # write a query to get brand info
    brands = Brand.query.all()

    for brand in brands:
        print "{}".format(brand.name)
        if brand.models:
            for model in brand.models:
                print "{} {}".format(model.year, model.name)
        else:
            print "Nothing in database!"

def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    brands = Brand.query.filter(Brand.name.like('%'+mystr+'%')).all()
    return brands



def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    models = (Model.query.filter(Model.year >= start_year, Model.year < end_year).all())
    return models