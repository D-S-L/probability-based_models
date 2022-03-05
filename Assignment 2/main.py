

import time




if __name__ == '__main__':
    start_time = time.time()
    print('---Filtering---')
    import Filtering
    print('\n---Prediction---')
    import Prediction
    print('\n---BayesianNetwork---')
    import BayesianNetwork

    print("\n--- %s seconds ---" % (time.time() - start_time))


