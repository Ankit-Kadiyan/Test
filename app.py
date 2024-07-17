from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Simple Calculator</h1>
        <form action="/calculate" method="post">
            <label for="num1">Number 1:</label>
            <input type="text" id="num1" name="num1"><br><br>
            <label for="num2">Number 2:</label>
            <input type="text" id="num2" name="num2"><br><br>
            <label for="operation">Operation:</label>
            <select id="operation" name="operation">
                <option value="add">Add</option>
                <option value="subtract">Subtract</option>
                <option value="multiply">Multiply</option>
                <option value="divide">Divide</option>
            </select><br><br>
            <input type="submit" value="Calculate">
        </form>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']
    
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2 if num2 != 0 else 'Error: Division by zero'
    else:
        result = 'Invalid operation'
    
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8082)
