-- 코드를 입력하세요
SELECT concat("/home/grep/src/",ugb.board_id,"/",file_id,file_name,file_ext) as FILE_PATH
from used_goods_board ugb
join used_goods_file ugf on ugb.board_id = ugf.board_id
where views in (select max(views) from used_goods_board)
order by file_id desc