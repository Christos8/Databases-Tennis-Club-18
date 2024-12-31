from entity_instances.field_in import FieldIn
from create_tables import CREATE_FIELD_TABLE
from insert_tables import INSERT_FIELD


class Field:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_FIELD_TABLE)

    def add_field(self, field: FieldIn):
        with self.connection:
            self.cursor.execute(INSERT_FIELD, (field.id, field.type, field.status))

    