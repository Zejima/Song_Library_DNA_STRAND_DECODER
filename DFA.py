from ArtistConnections import Vertex
from ArtistConnections import Edge
from SongLibrary import SongLibrary
from SongLibrary import Song
import ArtistConnections

class DFA:

    def __init__(self, s=None):
        self.start = s


    """
    Build the DFA graph from the figure in task 2

    """
    def build_DFA(self):
        v0=Vertex(0) #initialize vertex 0
        v1= Vertex(1) #initialize vertex 1
        v2=Vertex(2) #initialize vertex 2
        v3=Vertex(3) # initialize vertex 3
        v4=Vertex(4) # initialize vertex 4
        v5=Vertex(5) # initialize vertex 5
        v6=Vertex(6)# initialize vertex 6
        v7=Vertex(7) # initialize vertex 7

        v7.setAcceptingState() # sets v7 to the accepting state

        v0.addEdge(Edge("A",v1))  # adds edge from vertex 0 to vertex 1
        v1.addEdge(Edge("A",v1))  # adds edge from vertex 1 to vertex 1
        v1.addEdge(Edge("C",v2))  # adds edge from vertex 1 to vertex 2
        v2.addEdge(Edge("A",v3))  # adds edge from vertex 2 to vertex 3
        v3.addEdge(Edge("C",v4))  # adds edge from vertex 3 to vertex 4
        v4.addEdge(Edge("A",v5))  # adds edge from vertex 4 to vertex 5
        v5.addEdge(Edge("G",v6))  # adds edge from vertex 5 to vertex 6
        v6.addEdge(Edge("A",v7))  # adds edge from vertex 6 to vertex 7
        v7.addEdge(Edge("C",v2))  # adds edge from vertex 7 to vertex 2
        v7.addEdge(Edge("A",v1))  # adds edge from vertex 7 to vertex 1
        v5.addEdge(Edge("C",v4))  # adds edge from vertex 5 to vertex 4
        v5.addEdge(Edge("T",v1))  # adds edge from vertex 5 to vertex 1
        v3.addEdge(Edge("T",v1))  # adds edge from vertex 3 to vertex 1

        self.start=v0 # sets the start to verstx 0













        return

    """
    Test whether the input sequence seq will be accepted by the state machine
    return True if accept

    """
    def testMatch(self, seq):
        self.characters=list(seq)# makes a list out of the received variable seq
        self.current=self.start # sets the current to the first vertex

        for i in self.characters:  # iterates through the sequence and goes through the state machine
            if self.current==None: # if the next vertex is none then the sequence is not accepted by the state machine
                return False
            self.current=self.current.followEdge(i) # follows the vertex path
        if self.current==None:
            return  False

        if self.current.isAcceptingState: # if we are at the end of the sequence
            return True # the sequence is accepted
        else:
            return False

        #
        # Write your code here
        #

        return False

    """
    Test whether the one suffix of the input sequence seq will be accepted by the state machine
    return the index position if accept
    return -1 if not accept

    """
    def testAccept(self, seq):

        for i in range(0,len(seq)):
            if self.testMatch(seq[i:len(seq)])==True: # Within the for loop the string is cut shorter and shorter and
                                                    # sent through the testMatch method to see whether it will be
                                                    # accepted into the DFA state machine
                                                    # if accepted the variable i, representing the position will be
                                                    # returned , else -1 will be returned
                return i
        else:
            return -1





    """
    For every song in the song library array, test whether they will be accepted by the state machine
    Store the match index or -1 into the matchIndx array.
    Please make sure the order of songs in the songlibrary is the same as the input file

    """
    def testSongLibrary(self, song_lib):
        matchIndx = []

        for i in range (0, len(song_lib.songArray)):# Lineear Search through the song Array
            matchIndx.append(self.testAccept(song_lib.songArray[i].DNA))
                                                                # Through calling the test accept Method we
                                                                # create a array of the value og the postions
                                                                # returned byy the test matchIndx

        #
        # Write your code here
        #

        return matchIndx


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':

    dfa = DFA()
    dfa.build_DFA()
    print(dfa.testMatch('ACTTGCATGTGCGATCTGGATTTGGGCGGGGGCTAGTACAATCGTCGTTTCG'))
    print(dfa.testAccept("TTACACAGA"))
    song_lib = SongLibrary()
    song_lib.loadLibrary()
    print(dfa.testSongLibrary(song_lib))

    #dfa.testSongLibrary(SongLibrary)

    print("finish")