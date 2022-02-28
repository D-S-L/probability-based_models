
def prediction(evidence_data_add, prior, start_day, end_day):
    # you need to implement this method.

    x_prob_rain = []
    x_prob_rain_pre = []
    # x_prob_sunny[i] = 1 - x_prob_rain[i]
    umbrella ={1:(0.9,0.2),0:(0.1,0.8)}   #key: take umbrella or not, value: rain or not
    transition ={1:0.7,0:0.3}             #key: yesterday rain or not, value: the probability of rain in the next day

    # filtering
    with open(evidence_data_add) as f:
        cur_data = f.readline()

        while cur_data:
            evidence = cur_data.strip().split("\t")[1]   # obtain evidence
            evidence = 0 if evidence=='no umbrella' else 1
            previous_date_r = x_prob_rain_pre[-1] if x_prob_rain_pre else prior[0]   # obtain previous probability distribution

            T_r = previous_date_r*transition[1] + (1-previous_date_r)*transition[0]
            T_s = 1-T_r

            cur_e_r = umbrella[evidence][0]*T_r
            cur_e_s = umbrella[evidence][1]*T_s
            s = cur_e_r+cur_e_s
            cur_e_r = cur_e_r/s
            x_prob_rain_pre.append(cur_e_r)

            cur_data = f.readline()

    x_prob_rain_pre = x_prob_rain_pre[-1]

    # make prediction
    for i in range(start_day, end_day+1):
        previous_date_r = x_prob_rain[-1] if x_prob_rain else x_prob_rain_pre
        T_r = previous_date_r * transition[1] + (1 - previous_date_r) * transition[0]
        x_prob_rain.append(T_r)

    return x_prob_rain




# following lines are main function:
evidence_data_add = "data//assign2_umbrella.txt"
start_day = 101
end_day = 150
# the prior distribution on the initial state, P(X0). 50% rainy, and 50% sunny on day 0.
prior = [0.5, 0.5]

x_prob_rain=prediction(evidence_data_add, prior, start_day, end_day)
for i in range(start_day, end_day+1):
    print("Day " + str(i) + ": rain " + str(x_prob_rain[i-start_day]) + ", sunny " + str(1 - x_prob_rain[i-start_day]))
    # print("Day " + str(i+1) + ": rain " + str(x_prob_rain[i]) + ", sunny " + str(1 - x_prob_rain[i]))