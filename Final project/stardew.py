import knapsackDP as knapsackDP

reload(knapsackDP)

days = 28 # There is 28 days in a season

def optimizeCrop(season, items, weights, values):
    result = knapsackDP.knapsackDP(days, weights , values)
    print '\n'+season+' :'
    for i in range(0,len(items)):
        if(result.result[i] != 0):
            print(items[i]+' : '+str(int(result.result[i]))+' time(s)')
    print('Net Profit : '+str(result.f))
  

# Spring
items_spring = ['Blue Jazz', 'Cauliflower', 'Coffee Bean', 'Garlic', 'Green Bean', 'Kale', 'Parnsip', 'Potato', 
                'Rhubarb', 'Strawberry', 'Tulip', 'Unmilled Rice']
weights_spring = [7, 12, 28, 4, 28, 6, 4, 6, 13, 28, 6, 7]
values_spring = [20, 95, -1900, 20, 220, 40, 15, 30, 120, 620, 10, -10]
optimizeCrop('Spring', items_spring, weights_spring, values_spring)

# Summer
items_summer = ['Blueberry', 'Corn', 'Hops', 'Hot Pepper', 'Melon', 'Poppy', 'Radish', 'Red Cabbage', 'Starfruit', 
                'Summer Spangle', 'Sunflower', 'Tomato', 'Wheat']
weights_summer = [25, 26, 28, 26, 12, 7, 6, 9, 13, 8, 8, 27, 4]
values_summer = [520, 50, 390, 280, 170, 40, 50, 160, 350, 40, -120, 250, 15]
optimizeCrop('Summer', items_summer, weights_summer, values_summer)
        
# Fall
items_fall = ['Amarant', 'Artichoke', 'Beet', 'Bok Choy', 'Cranberries', 'Eggplant', 'Fairy Rose', 'Grape', 
              'Pumpkin', 'Yam']
weights_fall = [7,8,6,4,27,25,12,28,13,10]
values_fall = [80,130,80,30,510,280,90,500,220,100]
optimizeCrop('Fall', items_fall, weights_fall, values_fall)
        
# Winter
items_winter = ['Crocus', 'Snow Yam', 'Winter Root', 'Crystal Fruit']
weights_winter = [6 , 4, 5, 24]
values_winter = [90, 70, 75, 570]
optimizeCrop('Winter', items_winter, weights_winter, values_winter)