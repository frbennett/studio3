import flask
import time
import ex_script

from jinja2 import Environment
from jinja2.loaders import FileSystemLoader

app = flask.Flask(__name__)

@app.route('/yield')
def index():
    def inner():
        for x in range(5):
            time.sleep(1)
            yield '%s<br/>\n' % x
        yield 'hello \n'
        yield 'hello \n'
        yield from ex_script.atest()
    env = Environment(loader=FileSystemLoader('templates'))
    tmpl = env.get_template('result.html')
    return flask.Response(tmpl.generate(result=inner()))

app.run(debug=True)