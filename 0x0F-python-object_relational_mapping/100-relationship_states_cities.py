#!/usr/bin/python3

"""
Write a script that creates the State “California” with
the City “San Francisco” from the database
"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    s = Session()

    new_city = City(name="San Francisco",
                    state=State(name="California"))
    s.add(new_city)
    s.commit()
