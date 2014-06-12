def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if city is "Charlotte":
        return 183
    elif city is "Tampa":
        return 220
    elif city is "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    cost = days*40
    if days >= 7:
        return cost-40
    elif days >= 3:
        return cost-20
    else:
        return cost
    
def trip_cost(city, days, spending_money):
    return hotel_cost(days)+plane_ride_cost(city)+rental_car_cost(days)+spending_money
    
print trip_cost("Los Angeles",5,600)

8E5727

<a href="http://www.cost.eu/domains_actions/ict/Actions/IC1203" target="_blank"><img src="http://vgibox.eu/wp-content/uploads/2014/01/energic-logo-02.jpg" width="250" /></a>
<img src="http://vgibox.eu/wp-content/uploads/2014/04/ESF_white_logo.png" /><br>

L""nepold7
