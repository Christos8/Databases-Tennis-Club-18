SELECT_MEMBER_ID_FROM_USERNAME = "SELECT id FROM MEMBER WHERE username = (?)"
SELECT_COACH_ID_FROM_MEMBER_ID = "SELECT memberid FROM COACH WHERE memberid = (?)"
SELECT_USERNAME_FROM_USER_AUTH = "SELECT username FROM USER_AUTH WHERE username = (?)"
SELECT_PASSWORD_FROM_USER_AUTH = "SELECT password FROM USER_AUTH WHERE username = (?)"
SELECT_PLAYER_ID_FROM_MEMBER_ID = "SELECT memberid FROM player WHERE memberid = (?)"
SELECT_TOURNAMENTS_ALL = "SELECT * FROM TOURNAMENT"
SELECT_PROFILE = "SELECT * FROM MEMBER WHERE username = (?)"
SELECT_LESSONS = "SELECT * FROM LESSON WHERE coachid = (?)"

SELECT_COACHID = "SELECT id FROM MEMBER WHERE username = (?)"
SELECT_RESERVATION = "SELECT * FROM RESERVATION WHERE id = ?"

SELECT_ALL_LESSONS = "SELECT * FROM LESSON"