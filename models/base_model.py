#!/usr/bin/python3
import uuid
from datetime import datetime
from models.__init__ import storage

class BaseModel:
    """This class is base model of all other attribute and methods"""
    
    def __init__(self, *args, **kwargs):
        """
            instanciate a new base.
            A public class attribute that stores the id, time_created
            and updated, it is what makes the log of every object created
            Attributes:
            id: giving a univeral unique identifier
            created_at: date when the id was created
            updated_at: date when the id was updated
        """
        if kwargs is not None and kwargs != {}:
            
            for key, value in kwargs.items():
                if key == '__class__':
                    pass
                if key == 'id':
                    setattr (self, key, value)
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dTH:%M:%S.%f")
                    setattr (self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """ method updates public instance attribute"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ the unofficial string dictionary rep of the instance"""
        the_dict = self.__dict__.copy()
        the_dict["__class__"] = self.__class__.__name__
        the_dict["created_at"] = self.created_at.isoformat()
        the_dict["updated_at"] = self.updated_at.isoformat()
        the_dict["id"] = self.id
        return the_dict

    def __str__(self):
        """the unofficial str representation of an instnace"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__.copy()))
