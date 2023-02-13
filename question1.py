# question 1a
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += ['Oke']
# what was originally wrong with the exercise is that square brackets needed to be added around Oke for the object to appear on the list in the terminal
print(cheese)

# question 1b
cheese.extend(['Brie', 'Feta'])
print(cheese)
# extend method to add two different cheeses to the end of the list