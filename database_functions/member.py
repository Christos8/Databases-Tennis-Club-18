from entity_instances.member_in import MemberIn
from create_tables import CREATE_MEMBER_TABLE
from insert_tables import INSERT_MEMBER
from select_tables import SELECT_PROFILE, SELECT_MEMBER_BY_ID


class Member:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection
        self.cursor.executescript(CREATE_MEMBER_TABLE)

    def return_member(self, username):
        self.cursor.execute(SELECT_PROFILE, (username,))
        member_data = self.cursor.fetchone()
        member = MemberIn(member_data[1], member_data[2], member_data[3], member_data[4], member_data[5], member_data[6], member_data[7], member_data[8], member_data[0])
        return member

    def add_member(self, member: MemberIn):
        with self.connection:
            self.cursor.execute(INSERT_MEMBER, (member.name, member.surname, member.birthdate, member.phone, member.address, member.email, member.category, member.username))

    def get_member_by_id(self, memberid):
        self.cursor.execute(SELECT_MEMBER_BY_ID, (memberid,))
        member_data = self.cursor.fetchone()
        member = MemberIn(member_data[1], member_data[2], member_data[3], member_data[4], member_data[5], member_data[6], member_data[7], member_data[8], member_data[0])
        return member