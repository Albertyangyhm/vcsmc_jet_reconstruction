# Variational Combinatorial Sequential Monte Carlo Methods for Jet Reconstruction in Particle Physics

This repository contains a reference implementation of the methods described in:

Yang, Hanming, Moretti, Antonio Khalil, Macaluso, Sebastian, Chlenski, Philippe, Naesseth, Christian A., and Pe'er, Itsik. *Variational Pseudo Marginal Methods for Jet Reconstruction in Particle Physics*. Transactions on Machine Learning Research (TMLR), 2024. [OpenReview](https://openreview.net/forum?id=pCapRF2vFf)

If you use this repository, please cite the paper:

```bibtex
@article{yang2024variational,
  title={Variational Pseudo Marginal Methods for Jet Reconstruction in Particle Physics},
  author={Yang, Hanming and Moretti, Antonio Khalil and Macaluso, Sebastian and Chlenski, Philippe and Naesseth, Christian A. and Pe'er, Itsik},
  journal={Transactions on Machine Learning Research (TMLR)},
  year={2024},
  url={https://openreview.net/forum?id=pCapRF2vFf}
}
```

## Usage
To run, type the folowing in terminal: 

`python runner.py 
   --dataset=[some_data] 
   --n_particles=[some_number]
   --batch_size=[some_number]
   --learning_rate=[some_number]
   --twisting=[true/false]
   --num_epoch=100`   

This runner.py file assumes that all datasets (`ginkgo.p`, for example) are directly put under a folder called 'data'
     
