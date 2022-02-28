## Markov Chain

There is just status `transaction` in the model. Using the previous status to obtain the probability distribution of the next status
<img width="300" alt="image" src="https://user-images.githubusercontent.com/39432361/156053942-df9bccf4-b9a6-4fbc-a9cb-27e6547b5598.png">


## Hidden Markov Model(HMM) 
There are `evidence` for current and previous status, and use those evidence to obtain the probability distribution of `current hidden status`
therefore, for HMM, there are two sections:
1. Transition model 
2. Sensor model

<img width="300" alt="image" src="https://user-images.githubusercontent.com/39432361/156054422-1107bdc3-7f6a-43d0-9da4-859fb12f2c4a.png">.  <img width="300" alt="image" src="https://user-images.githubusercontent.com/39432361/156054610-bb709933-e119-40c8-a24f-4b920f8bbe24.png">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/39432361/156055962-b6624da2-fa37-449d-88f2-0cc8b62e7d64.png">

Example
<img width="400" alt="image" src="https://user-images.githubusercontent.com/39432361/156059123-4b9efb16-27bf-439e-afe8-7269dbbebee7.png">   <img width="400" alt="image" src="https://user-images.githubusercontent.com/39432361/156059179-588b8b33-4174-43dd-95f8-6da30be550c9.png">


