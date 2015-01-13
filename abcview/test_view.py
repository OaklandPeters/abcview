from collections import Sequence, MutableSequence
from view import (
    SequenceView, MutableSequenceView,
    SequenceSurrogate, MutableSequenceSurrogate,
)
from abcview import Cast

def test_cast():
    seq = list('mysubl')
    mseq = Cast(seq, MutableSequence)


    print()
    print("mseq:", type(mseq), mseq)
    print()
    import pdb
    pdb.set_trace()
    print()
    

    with Cast(seq, MutableSequence) as mseq:
        mseq.extend('ime')

        print()
        print("mseq:", type(mseq), mseq)
        print()
        import pdb
        pdb.set_trace()
        print()
        

def test_surrogate():

    seq = list('mysubl')
    # mseq = MutableSequenceSurrogate(seq)
    mseq = MutableSequenceView(seq)
    print("mseq: ", mseq)
    print("mseq[0]: ", mseq[0])
    mseq.extend('ime')
    print("Extended: ", mseq)





    print()
    print("mseq:", type(mseq), mseq)
    print()
    import pdb
    pdb.set_trace()
    print()

if __name__ == "__main__":
#    test_surrogate()
    test_cast()
