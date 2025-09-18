import capacity_model
import random 
import matplotlib.pyplot as plt

model = capacity_model.ConstModel(100, [10,30])

model_vals = []

# Tahoe variables
cwnd_tahoe = 1
cwnd_tahoe_hist = []
ssthres_tahoe = 50

# Reno variables  
cwnd_reno = 1
cwnd_reno_hist = []
ssthres_reno = 50

# Reno state variables
in_fast_recovery = False
dup_ack_count = 0

# iterate over 300 time units
for t in range(300):

    model_vals.append(model.eval(t))
    cwnd_tahoe_hist.append(cwnd_tahoe)
    cwnd_reno_hist.append(cwnd_reno)

    # Tahoe simulation
    #simulate timeout 
    if random.random() < model.timeout_prob(t, cwnd_tahoe):
        ssthres_tahoe = cwnd_tahoe / 2
        cwnd_tahoe = 1 

    # simulate 3 duplicate ack
    elif random.random() < model.dupacks_prob(t, cwnd_tahoe):
        ssthres_tahoe = cwnd_tahoe / 2
        cwnd_tahoe = 1  
    #non loss case
    else: 
        if cwnd_tahoe < ssthres_tahoe: #fast start
            cwnd_tahoe *= 2
        else: #additive increment 
            cwnd_tahoe += 1

    # Reno simulation
    #simulate timeout 
    if random.random() < model.timeout_prob(t, cwnd_reno):
        ssthres_reno = cwnd_reno / 2
        cwnd_reno = 1 
        in_fast_recovery = False
        dup_ack_count = 0

    # simulate 3 duplicate ack (Fast Recovery)
    elif random.random() < model.dupacks_prob(t, cwnd_reno):
        if not in_fast_recovery:
            # Enter Fast Recovery
            ssthres_reno = cwnd_reno / 2
            cwnd_reno = ssthres_reno + 3  # Set cwnd to ssthresh + 3
            in_fast_recovery = True
            dup_ack_count = 3
        else:
            # Already in Fast Recovery - inflate window
            cwnd_reno += 1
    #non loss case
    else: 
        if in_fast_recovery:
            # Fast Recovery: deflate window and exit
            cwnd_reno = ssthres_reno
            in_fast_recovery = False
            dup_ack_count = 0
        else:
            # Normal operation
            if cwnd_reno < ssthres_reno: #slow start
                cwnd_reno *= 2
            else: #congestion avoidance (additive increase)
                cwnd_reno += 1

        
print('total # segments sent with Tahoe = ', sum(cwnd_tahoe_hist))
print('total # segments sent with Reno = ', sum(cwnd_reno_hist))

t = list(range(300))

plt.plot(t, cwnd_tahoe_hist, label = 'CWND Tahoe', alpha=0.7)
plt.plot(t, cwnd_reno_hist, label = 'CWND Reno', alpha=0.7)
plt.plot(t, model_vals, label = 'Capacity Model')
plt.legend()
plt.xlabel('Time (RTT)')
plt.ylabel('# Segments (MSS)')
plt.title('TCP Tahoe vs Reno Congestion Control Comparison')

plt.show()