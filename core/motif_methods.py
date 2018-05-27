
import numpy as np


def motif_count_dict_to_array(motif_count_dict):
    ''' 
    converts the sampled counts of two or three 
    motifs from  multiple networks and shapes 
    in to array
    ---------------------------------------------
    arguments

        motif_count_dict:       

            {'00': [1506.0, 1036.0, ..., 38.0],
             '01': [1500.0, 1038.0, ..., 32.0],
              ...
             '04': [1494.0, 1043.0, ..., 38.0]}

    returns

       count_array:

            [[1506.0, 1036.0, ..., 38.0],
             [1500.0, 1038.0, ..., 32.0],
              ...
             [1494.0, 1043.0, ..., 38.0]]
    '''

    count_array = []
    for key,item in motif_count_dict.iteritems():
        count_array.append(item)

    return np.array(count_array)
    


def count_array_to_p_array(count_array):
    ''' 
    converts array of motif counts to array
    of relative probabilities of occurrence
    --------------------------------------------
    arguments

       count_array:

            [[1506.0, 1036.0, ..., 38.0],
             [1500.0, 1038.0, ..., 32.0],
              ...
             [1494.0, 1043.0, ..., 38.0]]

    returns

       p_array:

            [[0.512, 0.342, ..., 0.023],
             [0.505, 0.344, ..., 0.023],
              ... 
             [0.498, 0.348, ..., 0.024]]

    '''
    
    p_array = np.array([np.array(counts)/float(sum(counts)) \
                           for counts in count_array])

    return p_array



def motif_count_dict_to_p_array(motif_count_dict):

    p_array = count_array_to_p_array(
                motif_count_dict_to_array(motif_count_dict))

    return p_array



def expected_3motif_p_from_2motif_p(up,sp,rp):
    ''' 
    computes relative occurrences of three-neuron motifs 
    from 2 neuron motif occurrences
    --------------------------------------------
    arguments:

        up   probability for an unconnected pair
        sp   probability for a pair with a single connection
        rp   probability for reciprocally connected pair 

    returns:
    
        p    list of probabilities for each 3 neuron motif

    '''

    np.testing.assert_almost_equal(up+sp+rp, 1., decimal = 10)
    
    # for the calculation of expected motif occurence the
    # probability to have an edge from vertex 1 TO
    # vertex 2 is used rather than the probability
    # to have a single connection (see SI)
    spb = sp/2.

    # 16 motifs in total, later deleting first entry [0]
    # in list to have association motif 1 with [1].
    fact = range(17)
    ps = range(17)


    # motifs probabilities below were calculated 
    # from basic combinatorics considerations (see SI)
    fact[1], ps[1]    =   1, up**3 
    fact[2], ps[2]    =   6, up*up*spb
    fact[3], ps[3]    =   3, up*up*rp
    fact[4], ps[4]    =   3, spb*spb*up
    fact[5], ps[5]    =   3, spb*spb*up
    fact[6], ps[6]    =   6, spb*spb*up
    fact[7], ps[7]    =   6, spb*up*rp
    fact[8], ps[8]    =   6, spb*up*rp
    fact[9], ps[9]    =   3, rp*rp*up
    fact[10],ps[10]   =   6, spb**3   
    fact[11],ps[11]   =   2, spb**3    
    fact[12],ps[12]   =   3, spb*spb*rp
    fact[13],ps[13]   =   6, spb*spb*rp
    fact[14],ps[14]   =   3, spb*spb*rp
    fact[15],ps[15]   =   6, spb*rp*rp
    fact[16],ps[16]   =   1, rp**3     

    del fact[0],ps[0] 

    p = np.array([fact[i]*ps[i] for i in range(len(ps))])

    # factors should add up to 4^3 = 64, as for each
    # of the 3 neuron pairs in the motif there
    # are 4 possibile configurations:
    #
    #    unconnected (up), edge v1 -> v2 (spb=sp/2),
    #    edge v2 -> v1 (spb=sp/2), reciprocal (rp)
    assert sum(fact) == 64

    # p should add up to 1
    np.testing.assert_almost_equal(sum(p),1.0, decimal = 10,
                                   err_msg= 'Failed: sum(p) neq 1')

    print "Test: Sum of factors: ", sum(fact), " (Expected: 64)"
    print "Test: Sum of p: ", sum(p), " (Expected: 1.0)"
    
    return p


