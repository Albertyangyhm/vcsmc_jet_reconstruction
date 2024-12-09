# Variational Combinatorial Sequential Monte Carlo Methods for Jet Reconstruction in Particle Physics

This code provides a reference implementation of the publication:



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
     
