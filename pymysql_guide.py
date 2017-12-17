# Author Z
import pymysql

#想操作数据库之前要先连上数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='不能告诉你', db='也不能告诉你')

#连上数据库后就能操作数据库
# 不过在这之前需要一个游标，游标是什么呢？
# conn帮咱们连接，游标帮咱们存取数据，游标就相当于那只操作的手
# cursor = conn.cursor()

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

#怎么操作呢？用excute(),把那些sql语句往excute里面放就可以了。
#那返回值放入effect_row，这个返回值是什么呢？返回的是受影响的行数
#但这个时候数据库还没有受影响，要把它提交给数据库
# 修改：update
# effect_row = cursor.execute("update abc set abc = 'kkk'") ＃第一个abc是表名，name是其中的一个列
# 添加 insert
# effect_row = cursor.execute("insert into abc(nid,name) values (3,'abc')")
# 删除 delete
# effect_row = cursor.execute("delete from abc where nid=1")
# 查询 select
effect_row = cursor.execute("select * from abc")


# 对于查询来说，我们想获取查询过来的数据，就要用fetchall（）
# 打印出来的是一个元组
# 那我们怎么能把这个元组变成一个列表呢，那就把之前的cursor改一下，见第12行
# result = cursor.fetchall()
# print(result)

#fetchall拿到的是全部的数据，如果我们只要第一个数据，就用fetchone（）
# 这个fetchone还是那种只能取一遍的，再取就取到列表中下一个了。
# result = cursor.fetchone()
# print(result)
# result = cursor.fetchone()
# print(result)

#还有fetchmany，可以一次取好多次fetchone
result = cursor.fetchmany(1)
print(result)

# 这个游标为什么叫做游标呢，因为它可以移动,比如我们取了之前的数据之后，我们还可以把游标往前挪一下，再取一次，如下
cursor.scroll(-1,mode='relative')
result = cursor.fetchone()
print(result)

#还可以批量执行，用excutemany
#我们执行个批量插入
# effect_row = cursor.executemany("insert into abc(nid,name) values(%s,%s)",[(4,"abc"),(5,"kgh")])

# 打印一下，可以看到受影响的行数
# print(effect_row)


# 提交给数据库就需要commit,不然语句无法生效
conn.commit()

#可以看到最新插入数据库的自增id
# print(cursor.lastrowid)

# 关闭游标，收起那只手
cursor.close()

# 关闭连接
conn.close()


