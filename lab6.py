from flask import Blueprint, render_template, request, session, jsonify

lab6 = Blueprint('lab6', __name__)

# Данные об офисах в памяти (можно заменить на БД)
offices = [
    {"number": 101, "tenant": "", "price": 50000},
    {"number": 102, "tenant": "", "price": 45000},
    {"number": 103, "tenant": "", "price": 60000},
    {"number": 201, "tenant": "", "price": 55000},
    {"number": 202, "tenant": "", "price": 48000},
    {"number": 203, "tenant": "", "price": 52000},
    {"number": 301, "tenant": "", "price": 47000},
    {"number": 302, "tenant": "", "price": 53000}
]

@lab6.route('/')
def lab():
    return render_template('lab6/lab6.html')

@lab6.route('/json-rpc-api/', methods=['POST'])
def api():
    data = request.json
    
    if not data:
        return jsonify({
            'jsonrpc': '2.0',
            'error': {'code': -32600, 'message': 'Invalid Request'},
            'id': None
        })
    
    method = data.get('method')
    id = data.get('id', 1)
    
    if method == 'info':
        return jsonify({
            'jsonrpc': '2.0',
            'result': offices,
            'id': id
        })
    
    login = session.get('login')
    if not login:
        return jsonify({
            'jsonrpc': '2.0',
            'error': {'code': 1, 'message': 'Unauthorized'},
            'id': id
        })
    
    if method == 'booking':
        office_number = data.get('params')
        
        for office in offices:
            if office["number"] == office_number:
                if office["tenant"]:
                    return jsonify({
                        'jsonrpc': '2.0',
                        'error': {'code': 2, 'message': 'Already booked'},
                        'id': id
                    })
                office["tenant"] = login
                return jsonify({
                    'jsonrpc': '2.0',
                    'result': 'success',
                    'id': id
                })
        
        return jsonify({
            'jsonrpc': '2.0',
            'error': {'code': 5, 'message': 'Office not found'},
            'id': id
        })
    
    if method == 'cancelation':
        office_number = data.get('params')
        
        for office in offices:
            if office["number"] == office_number:
                if not office["tenant"]:
                    return jsonify({
                        'jsonrpc': '2.0',
                        'error': {'code': 3, 'message': 'Office is not booked'},
                        'id': id
                    })
                if office["tenant"] != login:
                    return jsonify({
                        'jsonrpc': '2.0',
                        'error': {'code': 4, 'message': "Cannot cancel other user's booking"},
                        'id': id
                    })
                office["tenant"] = ""
                return jsonify({
                    'jsonrpc': '2.0',
                    'result': 'success',
                    'id': id
                })
        
        return jsonify({
            'jsonrpc': '2.0',
            'error': {'code': 5, 'message': 'Office not found'},
            'id': id
        })
    
    return jsonify({
        'jsonrpc': '2.0',
        'error': {'code': -32601, 'message': 'Method not found'},
        'id': id
    })