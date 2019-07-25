from ffnet import ffnet, mlgraph, readdata, savenet
import time
import numpy as np



################## start training phase ##################


# start reading data
print "READING DATA..."
data = readdata( './files/data_rt_rr_statwosysdsk.txt', delimiter = ',' )
input =  data[:, 1:]
target = data[:, :1]

# Generate standard layered network architecture and create network
conec = mlgraph((input.shape[1],(input.shape[1]+1)/2,1))
net = ffnet(conec)

# training data start
print "TRAINING NETWORK..."
n=6168
net.randomweights()
st=time.time()
net.train_tnc(input[:n], target[:n])
el=time.time()-st
print "Time to train NN with %d examples: %0.3f sec"%(n,el)

# Save net
savenet(net,'./files/prcntrt_rr_statwosysdsk.network')

#test net

print "TESTING NETWORK..."
output, regression = net.test(input[n:], target[n:], iprint = 1)

y_act=np.array(target[n:])
y_prd=np.array(output)
err=abs(y_act-y_prd)/(y_act + 1)
print "Test error",sum(err)/len(err)*100


output, regression = net.test(input[:n], target[:n], iprint = 0)

y_act=np.array(target[:n])
y_prd=np.array(output)
err=abs(y_act-y_prd)/(y_act + 1)
print "Training error",sum(err)/len(err)*100


