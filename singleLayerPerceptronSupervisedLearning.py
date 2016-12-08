# weight update equation
# weight change = learning rate * (target output - actual output) * input
# w_i = r * (t - o) * x_i
# http://www.theprojectspot.com/tutorial-post/introduction-to-artificial-neural-networks-part-2-learning/8
import sys

# This models an AND gate, or a NOR gate

# initiate output threshold, learning rate, and start weights
threshold = 1
learningRate = 0.1
weights = [0.1, 0.1]

trainingData = [
    [ [0,0], [0] ],
    [ [0,1], [0] ],
    [ [1,0], [0] ],
    [ [1,1], [1] ]
]

''' NOR training data with bias unit (always outputs 1)
trainingData = [
    [ [0,0], [0] ],
    [ [0,1], [0] ],
    [ [1,0], [0] ],
    [ [1,1], [1] ]
]

'''
print "running through training data"
for x in trainingData:
    print x

#sys.exit()
'''
Now, we need to create a loop that we can break from later if our network
completes a cycle of the training data without any errors.
Then, we need a second loop that will iterate over each input
in the training data.
'''
while True:
    errorCount = 0
    # first loop
    for x in trainingData:
        print "Starting Weights " + str(weights)

        # calculate weighted sum of inputs and get output
        weightedSum = 0
        cur_weight = 0
        for i in x[0]: # for each input in  input set
            print "input=" + str(i)
            print "weight #" + str(cur_weight) + "=" + str(weights[cur_weight])
            weightedSum += i * weights[cur_weight]
            cur_weight = cur_weight + 1

        # calculate output
        output = 0
        if threshold <= weightedSum:
            output = 1

        print "Target output:  " + str(x[1][0])
        print "Actual output: " + str(output)

        # calculate error and adjust weights
        error = x[1][0] - output

        # increase error count for incorrect output
        if error != 0:
            errorCount = errorCount + 1

        # update weights
        cur_weight = 0
        for i in x[0]:
            # weightDif= learnRate * error * input
            weights[cur_weight] = weights[cur_weight] + learningRate * error * i
            cur_weight = cur_weight + 1

        print "New weights: " + str(weights)
        print "--------------"
    if (errorCount == 0):
        print "Final Weights: " + str(weights)
        sys.exit()
