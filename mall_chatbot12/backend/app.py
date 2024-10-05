'''
import firebase_admin
from firebase_admin import credentials, db
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r'D:\2ND YEAR\intel hack\intelday\mall_chatbot.py\chatbot-8b195-firebase-adminsdk-nulcq-8d6404e53d.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chatbot-8b195-default-rtdb.firebaseio.com/'
})

# Process user input
def process_query(query):
    tokens = query.lower().split()
    return tokens

# Find product and store information from Firebase
def find_product_details(query_tokens):
    ref = db.reference('products')
    results = set()
    related_results = set()

    try:
        products = ref.get()

        if products:
            for product_key, product in products.items():
                product_name = product.get('name', '').lower()

                match_found = any(token in product_name for token in query_tokens)
                if match_found:
                    results.add((
                        product['name'],
                        product['shopName'],
                        product['discount'],
                        product['floor'],
                        product['price'],
                        product['shopSector']
                    ))
                else:
                    if any(token in product_name.split() for token in query_tokens):
                        related_results.add((
                            product['name'],
                            product['shopName'],
                            product['discount'],
                            product['floor'],
                            product['price'],
                            product['shopSector']
                        ))

        if results:
            response = "\n".join([f"Product: {product_name} is available at {shop_name}, Floor: {floor}. Price: {price}, Discount: {discount}%, Shop Sector: {shop_sector}"
                                  for product_name, shop_name, discount, floor, price, shop_sector in results])
            return response
        elif related_results:
            related_response = "\n".join([f"Product: {product_name} is available at {shop_name}, Floor: {floor}. Price: {price}, Discount: {discount}%, Shop Sector: {shop_sector}"
                                           for product_name, shop_name, discount, floor, price, shop_sector in related_results])
            return f"Sorry, the product you're looking for is not available in the mall.\nHowever, you might be interested in the following related products:\n{related_response}"
        else:
            return "Sorry, the product you're looking for is not available in the mall."

    except Exception as e:
        return f"Error fetching data: {str(e)}"

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.get_json()
    query = data.get('query', '')
    tokens = process_query(query)
    response = find_product_details(tokens)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    

'''

import firebase_admin
from firebase_admin import credentials, db
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r'D:\2ND YEAR\intel hack\intelday\mall_chatbot.py\chatbot-8b195-firebase-adminsdk-nulcq-8d6404e53d.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chatbot-8b195-default-rtdb.firebaseio.com/'
})

# Process user input
def process_query(query):
    # Tokenize and remove common stop words
    stop_words = set(['the', 'is', 'at', 'which', 'on', 'and', 'a', 'to', 'in', 'for', 'with', 'of', 'as', 'this', 'by'])
    tokens = [token.lower() for token in query.split() if token.lower() not in stop_words]
    return tokens

# Find product and store information from Firebase
def find_product_details(query_tokens):
    ref = db.reference('products')
    results = []
    related_results = []

    try:
        products = ref.get()

        if products:
            for product_key, product in products.items():
                product_name = product.get('name', '').lower()

                # Check if any token matches the product name
                match_found = any(token in product_name for token in query_tokens)
                if match_found:
                    results.append({
                        'name': product['name'],
                        'shopName': product['shopName'],
                        'discount': product['discount'],
                        'floor': product['floor'],
                        'price': product['price'],
                        'shopSector': product['shopSector']
                    })
                else:
                    # Add to related products if there is some similarity
                    if any(token in product_name.split() for token in query_tokens):
                        related_results.append({
                            'name': product['name'],
                            'shopName': product['shopName'],
                            'discount': product['discount'],
                            'floor': product['floor'],
                            'price': product['price'],
                            'shopSector': product['shopSector']
                        })

        # Format the results for output
        if results:
            response = [f"**Product:** {product['name']} is available at **{product['shopName']}**, **Floor:** {product['floor']}. **Price:** ${product['price']}, **Discount:** {product['discount']}%, **Shop Sector:** {product['shopSector']}"
                        for product in results]
            return "\n".join(response)
        elif related_results:
            related_response = [f"**Product:** {product['name']} is available at **{product['shopName']}**, **Floor:** {product['floor']}. **Price:** ${product['price']}, **Discount:** {product['discount']}%, **Shop Sector:** {product['shopSector']}"
                                for product in related_results]
            return "Sorry, the product you're looking for is not available in the mall.\nHowever, you might be interested in the following related products:\n" + "\n".join(related_response)
        else:
            return "Sorry, the product you're looking for is not available in the mall."

    except Exception as e:
        return f"Error fetching data: {str(e)}"

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.get_json()
    query = data.get('query', '')
    tokens = process_query(query)
    response = find_product_details(tokens)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
