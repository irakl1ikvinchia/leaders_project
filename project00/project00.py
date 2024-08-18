def cakes(recipe, available):
    maximum = float("inf")
    for quantity, amount_needed in recipe.items():
        if quantity in available:
            amount_available = available[quantity]
        else:
            amount_available = 0
            
        cakes_quantity = amount_available // amount_needed
        
        if cakes_quantity < maximum:
            maximum = cakes_quantity
            
    return maximum