Database:
	
	users
		user_id - INT, PRIMARY KEY
		name - VARCHAR
		surname
		balance - DOUBLE
		/* Auth data: */
		access_token - VARCHAR
		token_expires - DATETIME
		secret - VARCHAR

		optional: Picture in FS

	hold
		user_id - INT, FOREIGN KEY
		category - INT, FOREIGN KEY
		count - INT


	transactions
		bet_id - INT, PRIMARY KEY
		user_id - INT, FOREIGN KEY `Users`
		timestamp - TIME
		round_id - INT, INDEX
		meme_category - INT, FOREIGN KEY `Meme_category.Meme_id`
		value - DOUBLE
		profit - DOUBLE
	
	meme_category
		Meme_id - INT, PRIMARY KEY
		Price - INT
		Name - VARCHAR

	transactions
		Log_id - INT, PRIMARY KEY
		Meme_id - INT, FOREIGN KEY `Meme_category`, INDEX
		Timestamp - TIME, INDEX
		Value - DOUBLE
		Difference - DOUBLE


SQL:


CREATE TABLE users (
	id INT, 
	name CHAR(255), 
	surname CHAR(255),
	balance DOUBLE PRECISION,
	access_token CHAR(255),
	secret CHAR(255),
	token_expires DATETIME,
	PRIMARY KEY (id)
);

CREATE TABLE meme_category (
	id INT AUTO_INCREMENT,
	name CHAR(255),
	price DOUBLE PRECISION,
	popularity DOUBLE PRECISION,
	PRIMARY KEY(id)
);

CREATE TABLE hold (
	user_id INT,
	category INT,
	count INT,
	FOREIGN KEY (category)
	REFERENCES meme_category(id),
	FOREIGN KEY (user_id)
	REFERENCES users(id)
);

CREATE TABLE changes (
	id INT AUTO_INCREMENT,
	meme_id INT,
	timestamp DATETIME,
	value DOUBLE PRECISION,
	difference DOUBLE PRECISION,
	PRIMARY KEY(id),
	FOREIGN KEY (meme_id)
	REFERENCES meme_category(id)
);

CREATE TABLE transactions (
	id INT AUTO_INCREMENT,
	user_id INT,
	timestamp DATETIME,
	round_id INT,
	meme_category INT,
	value DOUBLE,
	profit DOUBLE,
	PRIMARY KEY(id),
	FOREIGN KEY(user_id)
	REFERENCES users(id),
	FOREIGN KEY(meme_category)
	REFERENCES meme_category(id)
);


INSERT INTO meme_category (name) VALUES
('Finger'),
('Leo'),
('Robert'),
('SadMan'),
('Superbrain'),
('Vzuh')


