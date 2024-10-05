import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r'D:\2ND YEAR\intel hack\intelday\mall_chatbot.py\chatbot-8b195-firebase-adminsdk-nulcq-8d6404e53d.json')  # Update this path to your service account key
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chatbot-8b195-default-rtdb.firebaseio.com/'  # Your Firebase Database URL
})

# Process user input
def process_query(query):
    # Simple tokenization using split
    tokens = query.lower().split()
    return tokens

# Find product and store information from Firebase
def find_product_details(query_tokens):
    ref = db.reference('products')  # Reference to the products node
    results = set()  # Use a set to store unique results
    related_results = set()

    try:
        # Fetch all products from Firebase
        products = ref.get()

        if products:
            # Iterate through each product
            for product_key, product in products.items():
                product_name = product.get('name', '').lower()

                # Check if any token matches the product name
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
                    # Add to related products if there is some similarity
                    if any(token in product_name.split() for token in query_tokens):
                        related_results.add((
                            product['name'],
                            product['shopName'],
                            product['discount'],
                            product['floor'],
                            product['price'],
                            product['shopSector']
                        ))

        # Format the results for output
        if results:
            response = "\n".join([
                f"Product: {product_name} is available at {shop_name}, Floor: {floor}. Price: {price}, Discount: {discount}%, Shop Sector: {shop_sector}"
                for product_name, shop_name, discount, floor, price, shop_sector in results
            ])
            return response
        elif related_results:
            # If no exact matches were found, provide a specific message and show related products
            related_response = "\n".join([
                f"Product: {product_name} is available at {shop_name}, Floor: {floor}. Price: {price}, Discount: {discount}%, Shop Sector: {shop_sector}"
                for product_name, shop_name, discount, floor, price, shop_sector in related_results
            ])
            return f"Sorry, the product you're looking for is not available in the mall.\nHowever, you might be interested in the following related products:\n{related_response}"
        else:
            return "Sorry, the product you're looking for is not available in the mall."

    except Exception as e:
        return f"Error fetching data: {str(e)}"

# Chatbot loop
def chatbot():
    print("Welcome to the Mall Chatbot! How can I assist you today?")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        tokens = process_query(user_input)
        response = find_product_details(tokens)
        print(f"Bot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
