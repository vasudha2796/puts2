import statistics

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/add')
def addition():
    value1 = request.args.get('A', default=0, type=int)
    value2 = request.args.get('B', default=0, type=int)
    result = value1 + value2
    return '%d \n' % result

  
@app.route('/min')
def min():
    value = []
    value1 = str(request.args.get('A'))
    value1 = value1.split(',')
    try:
        value1.sort()
        for i in value1:
            i = float(i)
            value.append(i)
        value.sort()
        if value[0].is_integer():
            return '%d \n' % value[0]
        else:
            return '%f \n' % value[0]
    except ValueError:
        warning = "Enter numbers in the correct format"
        return warning


@app.route('/max')
def max():
    value = []
    value1 = str(request.args.get('A'))
    value1 = value1.split(',')
    try:
        value1.sort()
        for i in value1:
            i = float(i)
            value.append(i)
        value.sort()
        if value[-1].is_integer():
            return '%d \n' % value[-1]
        else:
            return '%f \n' % value[-1]
    except ValueError:
        warning = "Enter numbers in the correct format"
        return warning
      
      
@app.route('/median')
def median():
    value = []
    value1 = str(request.args.get('A'))
    value1 = value1.split(',')
    try:
        value1.sort()
        for i in value1:
            i = float(i)
            value.append(i)

        med = statistics.median(value)
        if med.is_integer():
            return '%d \n' % med
        else:
            return '%.3f \n' % med
    except ValueError:
        warning = "Enter numbers in the correct format"
        return warning
          
        
@app.route('/average')
def average():
    sum = 0
    value1 = str(request.args.get('A'))
    value1 = value1.split(',')
    try:
        for i in value1:
            sum = sum + float(i)

        averag = sum / len(value1)

        if averag.is_integer():
            return '%d \n' % averag
        else:
            return '%.3f \n' % averag
    except ValueError:
        warning = "Enter numbers in the correct format"
        return warning


@app.route('/mean')
def mean():
    sum = 0
    value1 = str(request.args.get('A'))
    value1 = value1.split(',')
    try:
        for i in value1:
            sum = sum + float(i)

        averag = sum / len(value1)

        if averag.is_integer():
            return '%d \n' % averag
        else:
            return '%.3f \n' % averag
    except ValueError:
        warning = "Enter numbers in the correct format"
        return warning


@app.route('/avg')
def avg():
    sum = 0
    value1 = str(request.args.get

                 ('A'))
    value1 = value1.split(',')
    try:
        for i in value1:
            sum = sum + float(i)

        averag = sum / len(value1)

        if averag.is_integer():
            return '%d \n' % averag
        else:
            return '%.3f \n' % averag
          
    except ValueError:
        warning = "Enter numbers in the correct format"
        return warning


if __name__ == "__main__":
    app.run()
