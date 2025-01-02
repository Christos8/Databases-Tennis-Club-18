from entity_instances.member_in import MemberIn
from create_tables import CREATE_MEMBER_TABLE
from insert_tables import INSERT_MEMBER


class Member:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_MEMBER_TABLE)

    def add_member(self, member: MemberIn):
        with self.connection:
            self.cursor.execute(INSERT_MEMBER, (member.name, member.surname, member.birthdate, member.phone, member.address, member.email, member.category, member.username))

    