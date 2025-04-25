# FYP_DS_Adnan
Movie Recommendation System
I did the coding in jupyter notebook.
This is a big dataset about 25Million rows
I used surprice library
but it got some memory issues for my system so 
I Used Anaconda Prompt to Install It into Jupyter’s Environment
still got issues for installing in base environment 
So I created a new Clean Environment
steps to do that are below
1. Open anaconda prompt
Code: conda create -n movielens_env python=3.10 -y

2. Activate the environment
Code: conda activate movielens_env

3. Install scikit-surprise (without breaking base!)
Code: conda install -c conda-forge scikit-surprise

4.  Install Jupyter into this environment
Code: conda install ipykernel -y
python -m ipykernel install --user --name=movielens_env --display-name "Python (MovieLens)"

5. Open Jupyter Notebook (same anaconda terminal)
Code: jupyter notebook

6. Test in Notebook
Steps:
- Open your notebook.
- Click on the kernel name (upper right corner or top toolbar: Kernel → Change Kernel).
- Select Python (MovieLens) from the list.

Next Execute ( just write this in your notbook cell)

code: from surprise import Dataset, Reader, SVD
print(" scikit-surprise is installed and working!")

now surprice will work in this envorinment

TO RUN THE STREMLIT JUST RUN CELL 38

THANKS :)  


   
