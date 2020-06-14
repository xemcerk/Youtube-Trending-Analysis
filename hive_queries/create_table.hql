-- create table and link to data file 
create external table us_videos(
    video_id string,
    trending_date int,
    title string,
    channel_title string,
    category_id int,
    publish_time string,
    views int,
    likes int,
    dislikes int,
    comment_count int,
    description string,
    delta_days int)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
stored as textfile
location '/tmp/hive/zkpk/ytb/';



