import aiomysql, uuid, time
from sanic import Sanic
from sanic.response import json, text
from ipku import CzIp
import datetime

Cz = CzIp()
_bh = {}


def address(ip):
    a = Cz.get_addr_by_ip(ip)
    # a = "香港 中国联通(香港)运营有限公司"
    # a = "美国 宾夕法尼亚州匹兹堡市"
    # a = "重庆市 电信"
    # a = "重庆市 重庆市"



    if a != '':
        a1 = a2 = ''
        sz = a.split(' ')
        print(sz)
        if len(sz) > 0:
            if sz[0].find('省') > 0:
                a1 = sz[0].split('省')[0] + '省'
            elif sz[0].find('国') > 0:
                a1 = sz[0].split('国')[0] + '国'
            elif sz[0].find('港') > 0:
                a1 = sz[0].split('港')[0] + '港'
            elif sz[0].find('市') > 0:
                a1 = sz[0].split('市')[0] + "市"
            else:
                a1 = sz[0]
        a2 = sz[1]
        if a1 == '' and a2 != '':
            a1 = a2
        if a2 == '' and a1 != '':
            a2 = a1
    # return a1, a2
    print(a1,a2)

    # if a != '':
    #     a1 = a2 = ''
    #     sz = a.split(' ')
    #     if len(sz) > 0:
    #         if sz[0].find('省') > 0:
    #             a1 = sz[0].split('省')[0] + '省'
    #             if sz[0].find('省') > 0:
    #                 a2 = sz[0].split('省')[1]
    #         else:
    #             if sz[0].find('市') > 0:
    #                 a2 = sz[0].split('市')[0] + '市'
    #     if a1 == '' and a2 != '':
    #         a1 = a2
    #     if a2 == '' and a1 != '':
    #         a2 = a1
    # # return a1, a2
    # print(a1,a2)

class sql:
    async def userlogin(self, user, pasd):
        pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                          user='root', password='1234',
                                          db='wx', )
        async with pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                sql_info = "select * from user where user='%s' and pasd='%s'" % (user, pasd)

                await cur.execute(sql_info)
                test = await cur.fetchone()  # fetchone
        pool.close()
        await pool.wait_closed()
        return test

    async def getddlist(self, token, ys, time1=None, time2=None, mark=None):  # 获取订单列表
        test = {}
        pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                          user='root', password='040404',
                                          db='wx', )
        async with pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                start = (int(ys) - 1) * 100
                end = int(ys) * 100
                sql_info = "select * from dd where token='%s'" % (token)
                if time1 and time2:
                    sql_info = sql_info + " and fbsj>%s and fbsj<%s" % (time1, time2)
                if mark:
                    sql_info = sql_info + " and sjh='%s' or ddbh='%s' or ddzt='%s'" % (mark, mark, mark)
                sql_info = sql_info + " limit %s,%s" % (start, end)
                await cur.execute(sql_info)
                test = await cur.fetchall()  # fetchone fetchall
                if len(test) == 0:
                    test = {}
        pool.close()
        await pool.wait_closed()
        return test

    async def getlslist(self, user, ys):
        pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                          user='root', password='1234',
                                          db='wx', )
        async with pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                start = (int(ys) - 1) * 100
                end = int(ys) * 100
                sql_info = "select * from dd where user='%s'  limit %s,%s " % (user, start, end)

                await cur.execute(sql_info)
                test = await cur.fetchall()  # fetchone fetchall
        pool.close()
        await pool.wait_closed()
        return test

    async def getczlist(self, user, ys):
        pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                          user='root', password='040404',
                                          db='wx', )
        async with pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                start = (ys - 1) * 100
                end = ys * 100
                sql_info = "select * from czjl where user='%s'  limit %s,%s " % (user, start, end)

                await cur.execute(sql_info)
                test = await cur.fetchall()  # fetchone fetchall
        pool.close()
        await pool.wait_closed()
        return test

    async def mark(self, token, ddbh, status, client=False):
        test = {"code": 0, "msg": "操作失败", "status": ""}
        pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                          user='root', password='040404',
                                          db='wx', )
        async with pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                if client:
                    sql_info = "update dd set ddzt='%s' where token='%s' and ddbh='%s'" % (status, token, ddbh)
                else:
                    sql_info = "update dd set sjmark='%s',ddzt='%s' where token='%s' and ddbh='%s'" % (
                    status, status, token, ddbh)
                isTrue = await cur.execute(sql_info)
                if isTrue:
                    test = {"code": 0, "msg": "操作成功", "status": "%s" % status}
        pool.close()
        await pool.wait_closed()
        return test

    async def getddstatus(self, token, ddbh):
        test = {"code": 0, "msg": "查询失败", "status": ""}
        pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                          user='root', password='040404',
                                          db='wx', )
        async with pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                sql_info = "select ddzt from dd where token='%s' and ddbh='%s'" % (token, ddbh)
                await cur.execute(sql_info)
                status = await cur.fetchone()  # fetchone fetchall
                if status is None:
                    status = {}
                test = {"code": 0, "msg": "查询成功", "status": "%s" % status.get('ddzt')}
        pool.close()
        await pool.wait_closed()
        return test

    async def updatetoken(self, user, token=None, newtoken=None, pasd=None, name=None, zfb=None, qq=None, wx=None):
        test = {"code": 0, "msg": "操作失败"}
        pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                          user='root', password='040404',
                                          db='wx', )
        async with pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                sql_info = "update user set"
                if token:
                    sql_info = sql_info + " token='%s'" % newtoken
                if pasd:
                    sql_info = sql_info + " pasd='%s'" % pasd
                if name:
                    sql_info = sql_info + " name='%s'" % name
                if zfb:
                    sql_info = sql_info + " zfb='%s'" % zfb
                if qq:
                    sql_info = sql_info + " qq='%s'" % qq
                if wx:
                    sql_info = sql_info + " wx='%s'" % wx
                sql_info = sql_info + " where user='%s'" % user

                isTrue = await cur.execute(sql_info)

                if isTrue:
                    test = {"code": 0, "msg": "操作成功"}
                    sql_info = "update dd set token='%s' where token='%s'" % (newtoken, token)

                    isTrue = await cur.execute(sql_info)
                    if isTrue:
                        test = {"code": 0, "msg": "操作成功"}
                    else:
                        test = {"code": 0, "msg": "操作失败"}
                else:
                    test = {"code": 0, "msg": "操作失败"}
        pool.close()
        await pool.wait_closed()
        return test

    async def gettask(self, token, zh):
        test = {}
        pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                          user='root', password='040404',
                                          db='wx', )
        async with pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                # jdsf,jdcs=address(ip)
                sql_info = "select dq from zh where zh='%s'" % zh
                isTrue = await cur.execute(sql_info)
                if isTrue > 0:
                    aa = await cur.fetchone()
                    jdsf = aa.get('dq')
                else:
                    pool.close()
                    await pool.wait_closed()
                    return test
                jdsj = (int(time.time()) - 310).__str__()
                sql_info = "update dd set ddzt='超时' where token='%s' and fbsf='%s'and fbsj<'%s' and ddzt!='超时' and ddzt!='成功' and ddzt!='失败'" % (
                token, jdsf, jdsj)
                await cur.execute(sql_info)
                sql_info = "select * from dd where token='%s' and ddzt='待接' and fbsf='%s'and fbsj>'%s'" % (
                token, jdsf, jdsj)
                isTrue = await cur.execute(sql_info)
                if isTrue > 0:
                    jdsj = int(time.time()).__str__()
                    test = await cur.fetchone()  # fetchone fetchall
                    id = test.get('id')
                    sqlexec = "update dd set jdsj='%s',ddzt='扫码',jdsf='%s',jdcs='%s',zh='%s' where id=%s" % (
                    jdsj, jdsf, jdsf, zh, id)
                    await cur.execute(sqlexec)
                    bhkey = '%s%s%s' % (
                    datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
                    bh = _bh.get(bhkey)
                    if bh is None:
                        bh = 1
                    else:
                        bh = int(bh) + 1
                    _bh[bhkey] = bh
                    test1 = {'id': test.get('ddbh'), 'url': test.get('url'), 'sjh': test.get('sjh'), 'bh': bh}
                    test = test1
        pool.close()
        await pool.wait_closed()
        return test

    async def TokenIsTrue(self, token):
        test = False
        pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                          user='root', password='040404',
                                          db='wx', )
        async with pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                sql_info = "select * from user where token='%s'" % (token)
                isTrue = await cur.execute(sql_info)
                if isTrue > 0:
                    test = True
        pool.close()
        await pool.wait_closed()
        return test

    async def countdq(self, token, sucess=False, time1=None, time2=None):
        test = {}
        pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                          user='root', password='040404',
                                          db='wx', )
        async with pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                sql_info = "select dq from dq"
                isTrue = await cur.execute(sql_info)
                if isTrue > 0:
                    _listawait = await cur.fetchall()
                    for i in _listawait:
                        dq = i.get('dq')
                        if sucess:
                            sql = "select count(*) as A from dd where jdsf='%s' and token='%s' and sjmark='成功'" % (
                            dq, token)
                        else:
                            sql = "select count(*) as A from dd where jdsf='%s' and token='%s' and sjmark='失败'" % (
                            dq, token)
                        if time1 and time2:
                            sql = sql + " and jdsj>%s and jdsj < %s" % (time1, time2)
                        await cur.execute(sql)

                        c = await cur.fetchone()
                        test[dq] = c.get('A', 0)

        pool.close()
        await pool.wait_closed()
        return test

    async def countzh(self, token, sucess=False, time1=None, time2=None):
        test = {}
        pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                          user='root', password='040404',
                                          db='wx', )
        async with pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                sql_info = "select zh from zh"
                isTrue = await cur.execute(sql_info)

                if isTrue > 0:
                    _listawait = await cur.fetchall()

                    for i in _listawait:

                        zh = i.get('zh')
                        if sucess:
                            sql = "select count(*) as A from dd where zh='%s' and token='%s' and sjmark='成功'" % (
                            zh, token)
                        else:
                            sql = "select count(*) as A from dd where zh='%s' and token='%s' and sjmark='失败'" % (
                            zh, token)
                        if time1 and time2:
                            sql = sql + " and jdsj>%s and jdsj < %s" % (time1, time2)
                        await cur.execute(sql)
                        c = await cur.fetchone()

                        test[zh] = c.get('A', 0)
        pool.close()
        await pool.wait_closed()
        return test

    async def addtask(self, token, url, sjh, ip):
        # 返回结果: {"code":0,"msg":"发布成功","number":"订单编号"}
        pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                          user='root', password='040404',
                                          db='wx', )

        isTrue = await self.TokenIsTrue(token)
        if isTrue == False:
            return 0

        async with pool.acquire() as conn:
            isTrue = 0
            async with conn.cursor(aiomysql.DictCursor) as cur:
                ddbh = uuid.uuid4().__str__()
                fbsf, fbcs = address(ip)

                fbsj = int(time.time()).__str__()
                sql_info = "INSERT INTO dd (ddbh,rwyj,sjh,url,fbsf,fbcs,fbsj,ddzt,token) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                           (ddbh, 0, sjh, url, fbsf, fbcs, fbsj, '待接', token)

                isTrue = await cur.execute(sql_info)

                if isTrue:
                    isTrue = ddbh

        pool.close()
        await pool.wait_closed()
        return isTrue

    async def adddq(self, dq, sc=False):
        res = '操作失败'
        pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                          user='root', password='040404',
                                          db='wx', )
        async with pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                if sc:
                    pass
                    sql_info = "DELETE FROM dq WHERE dq = '%s'" % dq
                else:
                    sql_info = "INSERT INTO dq (dq) VALUES ('%s')" % dq
                isTrue = await cur.execute(sql_info)
                if isTrue:
                    res = '操作成功'
        pool.close()
        await pool.wait_closed()
        return res

    async def addzh(self, zh, dq, sc=False):
        res = '操作失败'

        pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                          user='root', password='040404',
                                          db='wx', )
        async with pool.acquire() as conn:

            async with conn.cursor(aiomysql.DictCursor) as cur:
                if sc:
                    sql_info = "DELETE FROM zh WHERE zh = '%s'" % zh
                else:
                    sql_info = "INSERT INTO zh (zh,dq) VALUES ('%s','%s')" % (zh, dq)
                try:
                    isTrue = await cur.execute(sql_info)
                    if isTrue:
                        res = '操作成功'
                except:
                    res = '操作失败'
        pool.close()
        await pool.wait_closed()
        return res

    async def getcountlist(self, token, time1=None, time2=None):
        test = {}
        pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                          user='root', password='040404',
                                          db='wx', )
        async with pool.acquire() as conn:
            dj = sm = dqr = cs = cg = sb = zy = zs = 0
            async with conn.cursor(aiomysql.DictCursor) as cur:
                if time1 and time2:
                    sql_list = "select ddzt,sjmark from dd where token='%s' and fbsj>%s and fbsj<%s" % (
                    token, time1, time2)
                else:
                    sql_list = "select ddzt,sjmark from dd where token='%s'" % token
                await cur.execute(sql_list)

                list1 = await cur.fetchall()  # fetchone fetchall
                if list1 != ():
                    zs = len(list1)

                    for i in list1:
                        ddzt = i.get('ddzt')
                        sjmark = i.get('sjmark')

                        if ddzt == '待接':
                            dj = dj + 1
                            continue
                        if ddzt == '扫码':  # 判断扫码和时间
                            sm = sm + 1
                        if ddzt == '成功':
                            if sjmark == '成功':
                                cg = cg + 1
                            elif sjmark == '失败':
                                zy = zy + 1
                            else:
                                dqr = dqr + 1
                        if ddzt == '失败':
                            sb = sb + 1
                        if ddzt == '超时':
                            cs = cs + 1
                    test = {'dj': dj, 'sm': sm, 'dqr': dqr, 'cs': cs, 'cg': cg, 'sb': sb, 'zy': zy, 'zs': zs}
        pool.close()
        await pool.wait_closed()
        return test


app = Sanic("App Name")
Mysql = sql()


@app.post("/login")
async def login(request):
    user = request.form.get('user')
    pasd = request.form.get('pasd')
    if user and pasd:
        userinfo = await Mysql.userlogin(user, pasd)
        if userinfo is not None:
            response = json(userinfo)
            response.cookies['user'] = userinfo['user']
            response.cookies['user']['httponly'] = True
            return response
        else:
            userinfo = {}
            return json(userinfo)
    else:
        userinfo = {}
        return json(userinfo)


@app.post("/getddlist")
async def getddlist(request):
    #  user = request.cookies.get('token')
    ys = request.form.get('ys')
    token = request.form.get('token')
    time1 = request.form.get('time1')
    time2 = request.form.get('time2')
    mark = request.form.get('mark')
    if token and ys:
        ddlist = await Mysql.getddlist(token, ys, time1, time2, mark)
        if ddlist:
            response = json(ddlist)
        else:
            ddlist = {}
            response = json(ddlist)
    else:
        ddlist = {}
        response = json(ddlist)

    return response


@app.post("/getlslist")
async def getlslist(request):
    user = request.cookies.get('user')
    ys = request.form.get('ys')
    if user and ys:
        ddlist = await Mysql.getlslist(user, ys)
        if ddlist:
            response = json(ddlist)
    else:
        ddlist = {}
        response = json(ddlist)
    return response


@app.post("/getczlist")
async def getlslist(request):
    user = request.cookies.get('user')
    ys = request.form.get('ys')
    if user and ys:
        ddlist = await Mysql.getczlist(user, ys)
        if ddlist:
            response = json(ddlist)
    else:
        ddlist = {}
        response = json(ddlist)
    return response


@app.post("/m1")
async def mark(request):
    token = request.form.get('token')
    ddbh = request.form.get('number')
    status = request.form.get('status')
    if token and ddbh and status:
        mark = await Mysql.mark(token, ddbh, status)
        if mark:
            response = json(mark)
    else:
        mark = {}
        response = json(mark)
    return response


@app.post("/m2")
async def mark(request):
    token = request.form.get('token')
    ddbh = request.form.get('number')
    status = request.form.get('status')
    if token and ddbh and status:
        mark = await Mysql.mark(token, ddbh, status, True)
        if mark:
            response = json(mark)
    else:
        mark = {}
        response = json(mark)
    return response


@app.post("/m3")
async def getlslist(request):
    token = request.form.get('token')
    ddbh = request.form.get('number')
    if token and ddbh:
        ddlist = await Mysql.getddstatus(token, ddbh)
        if ddlist is not None:
            response = json(ddlist)
        else:
            ddlist = {}
            response = json(ddlist)
    else:
        ddlist = {}
        response = json(ddlist)
    return response


@app.post("/m4")
async def addtask(request):
    token = request.form.get('token')
    url = request.form.get('url')
    sjh = request.form.get('sjh')
    if token and url and sjh:
        task = await Mysql.addtask(token, url, sjh, request.ip)
        if task:
            response = json({"code": 0, "msg": "发布成功", "number": "%s" % task})
        else:
            response = json({"code": 0, "msg": "发布失败", "number": "0"})
    else:
        response = json({"code": 0, "msg": "发布失败", "number": "0"})
    return response


@app.post("/getliststatus")
async def getliststatus(request):
    token = request.form.get('token')
    time1 = request.form.get('time1')
    time2 = request.form.get('time2')

    if token is None:
        return json({})
    if token and time1 and time2:
        ddlist = await Mysql.getcountlist(token, time1, time2)
    else:
        ddlist = await Mysql.getcountlist(token)
    response = json(ddlist)
    return response


@app.post("/gettask")
async def gettask(request):
    token = request.form.get('token')
    zh = request.form.get('zh')
    if token is None or zh is None:
        return json({})
    taskinfo = await Mysql.gettask(token, zh)
    response = json(taskinfo)
    return response


@app.post("/getcountzh")
async def getcountzh(request):
    time1 = request.form.get('time1')
    token = request.form.get('token')
    time2 = request.form.get('time2')
    sucess = request.form.get('sucess')
    if token is None:
        return json({})
    if time1 is None or time2 is None:
        time1 = None
        time2 = None
    if sucess is None:
        sucess = False
    else:
        sucess = True
    taskinfo = await Mysql.countzh(token, sucess, time1, time2)

    response = json(taskinfo)
    return response


@app.post("/getcountdq")
async def getcountzh(request):
    time1 = request.form.get('time1')
    token = request.form.get('token')
    time2 = request.form.get('time2')
    sucess = request.form.get('sucess')
    if token is None:
        return json({})
    if time1 is None or time2 is None:
        time1 = None
        time2 = None
    if sucess is None:
        sucess = False
    else:
        sucess = True
    taskinfo = await Mysql.countdq(token, sucess, time1, time2)
    response = json(taskinfo)
    return response


@app.post("/updatetoken")
async def updatetoken(request):
    token = request.form.get('token')
    newtoken = request.form.get('newtoken')
    pasd = request.form.get('pasd')
    name = request.form.get('name')
    zfb = request.form.get('zfb')
    qq = request.form.get('qq')
    wx = request.form.get('wx')
    user = request.cookies.get('user')

    if token is None and newtoken is None and pasd is None and name is None and zfb is None and qq is None and wx is None and user is None:
        return json({})
    if user is None:
        return json({})
    taskinfo = await Mysql.updatetoken(user, token, newtoken, pasd, name, zfb, qq, wx)
    response = json(taskinfo)
    return response


@app.post("/adddq")
async def adddq(request):
    user = request.cookies.get('user')
    dq = request.form.get('dq')
    sc = request.form.get('sc')
    if user is None or dq is None:
        return text('操作失败')
    if sc is None:
        sc = False
    else:
        sc = True
    taskinfo = await Mysql.adddq(dq, sc)
    return text(taskinfo)


@app.post("/addzh")
async def addzh(request):
    user = request.cookies.get('user')
    zh = request.form.get('zh')
    dq = request.form.get('dq')
    sc = request.form.get('sc')
    if user is None or zh is None or dq is None:
        return text('操作失败')
    if sc is None:
        sc = False
    else:
        sc = True
    taskinfo = await Mysql.addzh(zh, dq, sc)
    return text(taskinfo)


# gettask
# 请求地址: http://服务器地址/wf/admin/src/php/upload.php

# 请求参数: token=秘钥&url=辅助链接&phone=手机号码

# 返回结果: {"code":0,"msg":"发布成功","number":"订单编号"}
if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=8000)
    ip = '128.90.199.125'
    address(ip)

#  await pool.wait_closed() #等待释放和关闭所有已获取连接的协同程序。应该在close（）之后调用，以等待实际的池关闭。
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test_example(loop))
