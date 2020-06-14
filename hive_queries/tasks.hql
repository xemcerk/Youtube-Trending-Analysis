
-- task 1
select title, views+likes+comment_count as pop from us_videos
order by pop desc
limit 5;

-- NULL check
select * from us_videos 
where title is NULL or title = '' or length(title)=0
limit 1;

-- task 3
select category_id, sum(views)+sum(likes)+sum(comment_count) as pop 
from us_videos
group by category_id
order by pop desc
limit 5; 

-- task 5
select video_id, count(*) as trending_stay from us_videos
group by video_id
order by trending_stay desc
limit 5;

-- task 6
select avg(delta_days) as avg_days from us_videos
group by category_id
order by avg_days desc
limit 5;