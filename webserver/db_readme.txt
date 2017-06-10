Database:
	
	Users
		User_id - INT, PRIMARY KEY
		Balance - INT
		/* Auth data: */
		VK_access_token - VARCHAR
		VK_token_expires - DATETIME

		API_access_token - VARCHAR
		API_token_expires - DATETIME

		Optional: Picture - BLOB

	Bets
		Bet_id - INT, PRIMARY KEY
		User_id - INT, FOREIGN KEY `Users`
		Timestamp - TIME
		Round_id - INT, INDEX
		Meme_category - INT, FOREIGN KEY `Meme_category.Meme_id`
		Value - ???
		Profit - INT
	
	Meme_category
		Meme_id - INT, PRIMARY KEY
		Pattern - BLOB

	Changelog
		Log_id - INT, PRIMARY KEY
		Meme_id - INT, FOREIGN KEY `Meme_category`, INDEX
		Timestamp - TIME, INDEX
		Value - DOUBLE
