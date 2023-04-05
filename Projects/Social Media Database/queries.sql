USE social_media;

-- find 5 oldest users
SELECT 
    *
FROM
    users
ORDER BY created_at
LIMIT 5;

-- most popular registation date
SELECT 
    DAYNAME(created_at) AS day_of_week, COUNT(*) AS how_many
FROM
    users
GROUP BY day_of_week
ORDER BY how_many DESC
LIMIT 2;

-- get data for photo with the highest score of likes
SELECT 
    photos.user_id,
    photos.photo_id,
    photos.image_url,
    photos.created_at,
    COUNT(*) AS likes_number
FROM
    photos
        JOIN
    likes ON likes.photo_id = photos.photo_id
GROUP BY photo_id
ORDER BY likes_number DESC
LIMIT 1;

-- get the user with the most liked photo
SELECT 
    username,
    photos.photo_id,
    photos.image_url,
    COUNT(*) AS likes_number
FROM
    photos
        JOIN
    likes ON likes.photo_id = photos.photo_id
        JOIN
    users ON photos.user_id = users.user_id
GROUP BY photo_id
ORDER BY likes_number DESC
LIMIT 1;

-- avg number of photos per user
SELECT 
    ((SELECT 
            COUNT(photo_id)
        FROM
            photos) / (SELECT 
            COUNT(user_id)
        FROM
            users)) AS avg_post;

-- 5 most popular tags
SELECT 
    tag_name, COUNT(*) AS number_used
FROM
    tags
        JOIN
    photo_tags ON tags.tag_id = photo_tags.tag_id
GROUP BY tag_name
ORDER BY number_used DESC
LIMIT 5;

-- find users that liked every photo
SELECT 
    username, COUNT(*) AS number_likes
FROM
    users
        JOIN
    likes ON users.user_id = likes.user_id
GROUP BY likes.user_id
HAVING number_likes = (SELECT 
        COUNT(*)
    FROM
        photos); 