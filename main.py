import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)
secret = 21

class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

your_guesses = []

class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

    def post(self):
        x = int(self.request.get("x"))
        your_guesses.append(x)
        if x == secret:
            self.write("You guessed it - congratulations! It's number: %s" % secret)
            self.write(" Number of attempts: %s" % len(your_guesses))
        elif x < secret:
            self.write("go up! Number of attempts: %s" % len(your_guesses))
            return self.render_template("hello.html")
        elif x > secret:
            self.write("go down! Number of attempts: %s" % len(your_guesses))
            return self.render_template("hello.html")



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)# Calculator_Post_Request
# Casino_post_request
