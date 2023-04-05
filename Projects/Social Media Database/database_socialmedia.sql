CREATE DATABASE social_media;

USE social_media;

CREATE TABLE users (
    user_id INTEGER AUTO_INCREMENT,
    username VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(), 
	PRIMARY KEY(user_id)
);
 
CREATE TABLE photos (
    photo_id INTEGER AUTO_INCREMENT,
    image_url VARCHAR(255) NOT NULL,
    user_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    PRIMARY KEY(photo_id)
);
 
CREATE TABLE comments (
    comment_id INTEGER AUTO_INCREMENT,
    comment_text VARCHAR(255) NOT NULL,
    photo_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY(photo_id) REFERENCES photos(photo_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    PRIMARY KEY(comment_id)
);
 
CREATE TABLE likes (
    user_id INTEGER NOT NULL,
    photo_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(photo_id) REFERENCES photos(photo_id),
    PRIMARY KEY(user_id, photo_id)
);
 
CREATE TABLE follows (
    follower_id INTEGER NOT NULL,
    followee_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY(follower_id) REFERENCES users(user_id),
    FOREIGN KEY(followee_id) REFERENCES users(user_id),
    PRIMARY KEY(follower_id, followee_id)
);
 
CREATE TABLE tags (
  tag_id INTEGER AUTO_INCREMENT,
  tag_name VARCHAR(255) UNIQUE,
  created_at TIMESTAMP DEFAULT NOW(),
  PRIMARY KEY(tag_id)
);
 
CREATE TABLE photo_tags (
    photo_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    FOREIGN KEY(photo_id) REFERENCES photos(photo_id),
    FOREIGN KEY(tag_id) REFERENCES tags(tag_id),
    PRIMARY KEY(photo_id, tag_id)
);