SELECT_MEMBER_ID_FROM_USERNAME = "SELECT id FROM MEMBER WHERE username = (?)"
SELECT_COACH_ID_FROM_MEMBER_ID = "SELECT memberid FROM COACH WHERE memberid = (?)"
SELECT_USERNAME_FROM_USER_AUTH = "SELECT username FROM USER_AUTH WHERE username = (?)"
SELECT_PASSWORD_FROM_USER_AUTH = "SELECT password FROM USER_AUTH WHERE username = (?)"
SELECT_PLAYER_ID_FROM_MEMBER_ID = "SELECT memberid FROM player WHERE memberid = (?)"
SELECT_TOURNAMENTS_ALL = "SELECT * FROM TOURNAMENT"
SELECT_PROFILE = "SELECT * FROM MEMBER WHERE username = (?)"
SELECT_LESSONS = "SELECT * FROM LESSON WHERE coachid = (?)"
SELECT_TOURNAMENT_PARTICIPATION = "SELECT * FROM TOURNAMENT_PARTICIPATION WHERE playerid = (?) AND tournamentid = (?)"
SELECT_TOURNAMENT_PARTICIPATION_PLAYERID = "SELECT tournamentid FROM TOURNAMENT_PARTICIPATION WHERE playerid = (?)"
SELECT_TOURNAMENT_FROM_ID = "SELECT * FROM TOURNAMENT WHERE id = (?)"
SELECT_COACHID = "SELECT id FROM MEMBER WHERE username = (?)"
SELECT_RESERVATION = "SELECT * FROM RESERVATION WHERE id = ?"
SELECT_ALL_EQUIPMENT = "SELECT * FROM EQUIPMENT"
SELECT_EQUIPMENT_FROM_ID = "SELECT * FROM EQUIPMENT WHERE id = (?)"
SELECT_EQUIPMENT_RENTAL_FROM_PLAYERID = "SELECT * FROM equipment_rental WHERE playerID = (?)"
SELECT_ALL_LESSONS = "SELECT * FROM LESSON"
SELECT_LESSON_PARTICIPATION = "SELECT * FROM LESSON_PARTICIPATION WHERE playerid = (?) AND lessonid = (?)"
SELECT_ACTIVE_SUBSCRIPTION = "SELECT * FROM PLAYER_SUBSCRIPTION WHERE playerid = (?)"
SELECT_PLAYERID = "SELECT id FROM MEMBER WHERE username = (?)"