from flask import Flask, jsonify, request

app = Flask(__name__)

notifications = []
next_id = 1

@app.route('/notify', methods=['GET'])
def get_notifications():
    return jsonify({'notifications': notifications})

@app.route('/notify', methods=['POST'])
def create_notification():
    global next_id
    data = request.json
    notification = {
        'id': next_id,
        'message': data.get('message', ''),
        'type': data.get('type', 'info'),
        'user': data.get('user', 'general'),
        'read': False,
        'date': data.get('date', '')
    }
    next_id += 1
    notifications.append(notification)
    return jsonify(notification), 201

@app.route('/notify/<int:id>', methods=['PUT'])
def update_notification(id):
    notification = next((n for n in notifications if n['id'] == id), None)
    if not notification:
        return jsonify({'error': 'Notification not found'}), 404
    
    data = request.json
    if 'read' in data:
        notification['read'] = data['read']
    if 'message' in data:
        notification['message'] = data['message']
    
    return jsonify(notification)

@app.route('/notify/<int:id>', methods=['DELETE'])
def delete_notification(id):
    global notifications
    notification = next((n for n in notifications if n['id'] == id), None)
    if not notification:
        return jsonify({'error': 'Notification not found'}), 404
    
    notifications = [n for n in notifications if n['id'] != id]
    return jsonify({'message': 'Notification deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8004)