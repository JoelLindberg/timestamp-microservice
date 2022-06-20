class JsDatePattern1:
    regex = '[0-9]{2} [\w]+ [0-9]{4}, GMT'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value