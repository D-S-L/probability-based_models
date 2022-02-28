## Markov Chain

There is just status `transaction` in the model. Using the previous status to obtain the probability distribution of the next status
<img width="1098" alt="image" src="https://user-images.githubusercontent.com/39432361/156053942-df9bccf4-b9a6-4fbc-a9cb-27e6547b5598.png">


## Hidden Markov Model(HMM) 
There are `evidence` for current and previous status, and use those evidence to obtain the probability distribution of `current hidden status`
therefore, for HMM, there are two sections:
1. Transition model 
2. Sensor model
