import web

render = web.template.render('templates')
urls = (
    '/add', 'add',
    '/index', 'index',
    '/(.*)', 'hello'

)
app = web.application(urls, globals())


class hello:
    def GET(self, name):
        return  render.temp01(name)
        # return open(r'html01.html','r').read()

class index:
    def GET(self):
        return web.ctx.env

    def POST(self):
        query = web.input()
        return query

class blog:
    def POST(self):
        query = web.input()
        return query


class add:
    def GET(self):

        return web.seeother('http://www.baidu.com')

if __name__ == "__main__":
    app.run()