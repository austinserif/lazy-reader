"""file for profile class definition"""

class Profile:
    """Profile Class is instantiated with two string inputs, usually a 
    specific key-value pair from the entity dictionary returned by 
    Article.get_ents()"""
    def __init__(self, entity: str, entity_type: str):
        self.entity = entity
        self.entity_type = entity_type

    @classmethod
    def new(self, entity: str, entity_type: str) -> 'Profile':
        """takes an entity and entity_type, and returns instance of a Profile"""
        return Profile(entity, entity_type)
    
    
