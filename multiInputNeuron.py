
def ele_mul(array, number):
    out = list()
    for i in range(len(array)):
        out.append(array[i] * number)

    return out

def ele_sub(arr1, arr2):
    result = list()
    for i in range(len(arr1)):
        result.append(arr1[i] - arr2[i])

    return result

def neuron(input_datapoints, weights):
    output = 0
    for i in range(len(input_datapoints)):
        output += (input_datapoints[i] * weights[i])

    return output

# Assuming ball speed, bat speed, and wind speed decides distance a ball will travel
goal = 100      # meter
alpha = 0.0001     # learning rate

ball_speed = 25     # meter/sec
bat_speed = 5.55    # meter/sec
wind_speed = 1.38   # meter/sec

data_in = [bat_speed, ball_speed, wind_speed]

# initial value of weight is just some random number
weight = [-.9, .3, .5]

for i in range(100):
    print(f"Weight: {weight}")
    pred = neuron(data_in, weight)
    error = (pred - goal) ** 2
    derivative = ele_mul(data_in, (pred - goal))
    weight = ele_sub(weight, ele_mul(derivative, alpha))
    print(f"Error: {error}, Prediction: {pred}, Goal: {goal}")
    print(f"Derivative: {derivative} \n")


# Try changing alpha and see the result, you'll know the importance of setting learning rate

















