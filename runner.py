import logging
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # FATAL
logging.getLogger('tensorflow').setLevel(logging.FATAL)
import numpy as np
import argparse
import pandas as pd
import random

# export KMP_DUPLICATE_LIB_OK=TRUE

# python runner.py --dataset ginkgo --num_epoch 200 --n_particles 128 --learning_rate 0.001

def parse_args():
    parser = argparse.ArgumentParser(
                        description='Variational Combinatorial Sequential Monte Carlo')
    parser.add_argument('--dataset',
                        help='benchmark dataset to use.',
                        default='ginkgo')
    parser.add_argument('--n_particles',
                        type=int,
                        help='number of SMC samples.',
                        default=128)
    parser.add_argument('--batch_size',
                        type=int,
                        help='number of sites on genome per batch.',
                        default=256)
    parser.add_argument('--learning_rate',
                        type=float,
                        help='Learning rate.',
                        default=0.01)
    parser.add_argument('--num_epoch',
                        type=int,
                        help='number of epoches to train.',
                        default=100)
    parser.add_argument('--optimizer',
                       type=str,
                       help='Optimizer for Training',
                       default='GradientDescentOptimizer')
    parser.add_argument('--branch_prior',
                       type=float,
                       help='Hyperparameter for branch length initialization.',
                       default=np.log(5))
    parser.add_argument('--lambda_prior',
                       type=float,
                       help='Hyperparameter for branch length initialization.',
                       default=3)
    parser.add_argument('--decay_prior',
                       type=float,
                       help='Hyperparameter for branch length initialization.',
                       default=np.log(10))
    parser.add_argument('--M',
                       type=int,
                       help='number of subparticles to compute look-ahead particles',
                       default=10)
    parser.add_argument('--nested', 
                       default=False, 
                       type=lambda x: (str(x).lower() == 'true'))
    parser.add_argument('--jcmodel', 
                       default=False, 
                       type=lambda x: (str(x).lower() == 'true'))
    parser.add_argument('--memory_optimization',
                       help='Use memory optimization?',
                       default='on')


    args = parser.parse_args()
    return args


if __name__ == "__main__":

    ginkgo = True

    args = parse_args()

    exec(args.dataset + ' = True')

    if ginkgo:
        all_datadict = pd.read_pickle('data/gingko/any_25m2p5dp2.p')
        decay_params = []
        leafNums = []
        for i in range(5):
            curr_data = all_datadict[i]
            print(curr_data.keys())
            if args.nested == True:
                import vncsmc as vcsmc
            elif not ginkgo:
                import vcsmc as vcsmc
            elif ginkgo:
                import jet_vcsmc as vcsmc


            #pdb.set_trace()
            vcsmc = vcsmc.VCSMC(curr_data, K=args.n_particles, args=args)

            param = vcsmc.train(epochs=args.num_epoch, batch_size=args.batch_size, learning_rate=args.learning_rate, memory_optimization=args.memory_optimization)
            
            print("ground truth llh", curr_data['llh_sum'])
            print("ground truth decay parameter", curr_data['decay_rate'])
            decay_params.append(param)
            leafNums.append(curr_data['data'].shape[0])

        print(decay_params)
        print("final estimate: " + str(np.average(decay_params)))
        print(leafNums)
    else:    
        if args.nested == True:
            import vncsmc as vcsmc
        elif not ginkgo:
            import vcsmc as vcsmc
        elif ginkgo:
            import jet_vcsmc as vcsmc


        #pdb.set_trace()
        vcsmc = vcsmc.VCSMC(datadict, K=args.n_particles, args=args)

        param = vcsmc.train(epochs=args.num_epoch, batch_size=args.batch_size, learning_rate=args.learning_rate, memory_optimization=args.memory_optimization)
