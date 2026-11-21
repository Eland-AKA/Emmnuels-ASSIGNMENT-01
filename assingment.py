store_name = "Quad E"
customer_name = "Mr Daniel"
product_name = "Flipper Zero"
unit_price = 899999.99
items_purchased = 1
total_stock = 5
delivery_fee = 5000.00
payment_confirmed = True

subtotal = unit_price * items_purchased 
grand_total = subtotal + delivery_fee
average_cost_per_item = grand_total / items_purchased
remaining_stock = total_stock - items_purchased
if payment_confirmed:
    payment_status = "Paid"
else:
    payment_status = "Pending"
    
print("QUAD E RECEIPT")
print("Customer Name:", customer_name)
print("Product:", product_name)
print("Unit Price: ₦", unit_price)
print("Quantity Purchased:", items_purchased)
print("Subtotal: ₦", subtotal)
print("Delivery Fee: ₦", delivery_fee)
print("Grand Total: ₦", grand_total)
print("Average Cost Per Item: ₦", average_cost_per_item)
print("Remaining Stock:", remaining_stock)
print("Payment Status:", payment_status)