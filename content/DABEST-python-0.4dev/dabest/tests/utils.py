def create_demo_dataset(seed=9999, N=20):
    
    import numpy as np
    import pandas as pd
    from scipy.stats import norm # Used in generation of populations.

    np.random.seed(9999) # Fix the seed so the results are replicable.
    # pop_size = 10000 # Size of each population.

    # Create samples
    c1 = norm.rvs(loc=3, scale=0.4, size=N)
    c2 = norm.rvs(loc=3.5, scale=0.75, size=N)
    c3 = norm.rvs(loc=3.25, scale=0.4, size=N)

    t1 = norm.rvs(loc=3.5, scale=0.5, size=N)
    t2 = norm.rvs(loc=2.5, scale=0.6, size=N)
    t3 = norm.rvs(loc=3, scale=0.75, size=N)
    t4 = norm.rvs(loc=3.5, scale=0.75, size=N)
    t5 = norm.rvs(loc=3.25, scale=0.4, size=N)
    t6 = norm.rvs(loc=3.25, scale=0.4, size=N)


    # Add a `gender` column for coloring the data.
    females = np.repeat('Female', N/2).tolist()
    males = np.repeat('Male', N/2).tolist()
    gender = females + males

    # Add an `id` column for paired data plotting. 
    id_col = pd.Series(range(1, N+1))

    # Combine samples and gender into a DataFrame.
    df = pd.DataFrame({'Control 1' : c1,     'Test 1' : t1,
                       'Control 2' : c2,     'Test 2' : t2,
                       'Control 3' : c3,     'Test 3' : t3,
                       'Test 4'    : t4,     'Test 5' : t5, 'Test 6' : t6,
                       'Gender'    : gender, 'ID'  : id_col
                      })
                      
    return df



def create_demo_dataset_rm(seed=9999, N=20):
    
    import numpy as np
    import pandas as pd
    from scipy.stats import norm # Used in generation of populations.

    np.random.seed(9999) # Fix the seed so the results are replicable.
    # pop_size = 10000 # Size of each population.

    # Create samples
    timepoint0 = norm.rvs(loc=3, scale=0.4, size=N)
    timepoint1 = norm.rvs(loc=3.5, scale=0.75, size=N)
    timepoint2 = norm.rvs(loc=3.25, scale=0.4, size=N)
    timepoint3 = norm.rvs(loc=3.5, scale=0.5, size=N)
    timepoint4 = norm.rvs(loc=2.5, scale=0.6, size=N)
    timepoint5 = norm.rvs(loc=3, scale=0.75, size=N)
    timepoint6 = norm.rvs(loc=3.5, scale=0.75, size=N)
    timepoint7 = norm.rvs(loc=3.25, scale=0.4, size=N)
    timepoint8 = norm.rvs(loc=3.25, scale=0.4, size=N)


    # Add a `gender` column for coloring the data.
    grp1 = np.repeat('Group 1', N/2).tolist()
    grp2 = np.repeat('Group 2', N/2).tolist()
    grp = grp1 + grp2

    # Add an `id` column for paired data plotting. 
    id_col = pd.Series(range(1, N+1))

    # Combine samples and gender into a DataFrame.
    df = pd.DataFrame({'Time Point 0' : timepoint0,     
                       'Time Point 1' : timepoint1,
                       'Time Point 2' : timepoint2,     
                       'Time Point 3' : timepoint3,
                       'Time Point 4' : timepoint4,     
                       'Time Point 5' : timepoint5,
                       'Time Point 6' : timepoint6,     
                       'Time Point 7' : timepoint7, 
                       'Time Point 8' : timepoint8,
                       'Group'        : grp, 
                       'ID'           : id_col
                      })
                      
    return df


def create_demo_dataset_delta(seed=9999, N=20):
    
    import numpy as np
    import pandas as pd
    from scipy.stats import norm # Used in generation of populations.

    np.random.seed(seed) # Fix the seed so the results are replicable.
    # pop_size = 10000 # Size of each population.

    from scipy.stats import norm # Used in generation of populations.

    # Create samples
    y = norm.rvs(loc=3, scale=0.4, size=N*2)

    # Add experiment column
    e1 = np.repeat('Control', N).tolist()
    e2 = np.repeat('Test', N).tolist()
    experiment = e1 + e2 

    # Add a `Light` column as the first variable
    light = []
    for i in range(N):
        light.append('L1')
        light.append('L2')

    # Add a `genotype` column as the second variable
    g1 = np.repeat('G1', N/2).tolist()
    g2 = np.repeat('G2', N/2).tolist()
    g3 = np.repeat('G3', N).tolist()
    genotype = g1 + g2 + g3

    # Add an `id` column for paired data plotting.
    id_col = []
    for i in range(N):
        id_col.append(i)
        id_col.append(i)

    # Combine samples and gender into a DataFrame.
    df = pd.DataFrame({'ID'        : id_col,
                      'Light'      : light,
                       'Genotype'  : genotype, 
                       'Experiment': experiment,
                       'Y'         : y
                    })
                      
    return df


def get_swarm_yspans(coll, round_result=False, decimals=12):
    """
    Given a matplotlib Collection, will obtain the y spans
    for the collection. Will return None if this fails.
    Modified from `get_swarm_spans` in plot_tools.py.
    """
    import numpy as np
    _, y = np.array(coll.get_offsets()).T
    try:
        if round_result:
            return np.around(y.min(), decimals), np.around(y.max(),decimals)
        else:
            return y.min(), y.max()
    except ValueError:
        return None
        
        
        
# def create_dummy_dataset(seed=None, n=30, base_mean=0,
#                          plus_minus=5, expt_groups=7,
#                          scale_means=1., scale_std=1.):
#     """
#     Creates a dummy dataset for plotting.
#     Returns the seed used to generate the random numbers,
#     the maximum possible difference between mean differences,
#     and the dataset itself.
#     """
#     import numpy as np
#     import scipy as sp
#     import pandas as pd
# 
#     # Set a random seed.
#     if seed is None:
#         random_seed = np.random.randint(low=1, high=1000, size=1)[0]
#     else:
#         if isinstance(seed, int):
#             random_seed = seed
#         else:
#             raise TypeError('{} is not an integer.'.format(seed))
# 
#     # Generate a set of random means
#     np.random.seed(random_seed)
#     MEANS = np.repeat(base_mean, expt_groups) + \
#             np.random.uniform(base_mean-plus_minus, base_mean+plus_minus,
#                               expt_groups) * scale_means
#     SCALES = np.random.random(size=expt_groups) * scale_std
# 
#     max_mean_diff = np.ptp(MEANS)
# 
#     dataset = list()
#     for i, m in enumerate(MEANS):
#         pop = sp.stats.norm.rvs(loc=m, scale=SCALES[i], size=10000)
#         sample = np.random.choice(pop, size=n, replace=False)
#         dataset.append(sample)
# 
#     df = pd.DataFrame(dataset).T
#     df["idcol"] = pd.Series(range(1, n+1))
#     df.columns = [str(c) for c in df.columns]
# 
#     return random_seed, max_mean_diff, df
