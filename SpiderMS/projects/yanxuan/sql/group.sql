drop table if exists db_yanxuan.group;
CREATE TABLE db_yanxuan.group
(
    id              INT(11)      NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '自增主键',
    name            VARCHAR(255) COMMENT '目录名称',
    createTime      TIMESTAMP COMMENT '数据创建时间'default now(),
    updateTime      TIMESTAMP COMMENT '数据最后一次更新时间' default now()
);

truncate  table  db_yanxuan.group;

select
       *
from
     db_yanxuan.group;

