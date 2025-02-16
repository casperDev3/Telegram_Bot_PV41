def formatter_msg_with_product(product: dict) -> str:
    return (f"🎒 {product['title']}\n"
            f"💰 {product['price']} USD\n"
            f"📝 {product['description']}\n"
            f"📦 {product['category']}\n"
            f"🌟 {product['rating']['rate']} ({product['rating']['count']} ratings)\n")

def formatter_msg_with_all_categories(category: dict) -> str:
    text = ""
    for cat in category:
        text += f"🎒 {cat}\n"
    return text