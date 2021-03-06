import pytest
from ..LinkedListUnrolled import *

#####
# Node
#

@pytest.fixture()
def n():
    n = NodeUnrolled()
    return n

class Test_create_node(object):
    def test_type(self, n):
        assert isinstance(n, NodeUnrolled)
        
    def test_max_elements(self, n):
        assert n.max_elements == 4
        
    def test_num_elements(self, n):
        assert n.num_elements == 0
        
    def test_values(self, n):
        assert n.values == [None, None, None, None]

    def test_next(self, n):
        assert n.next is None
        
class Test_put_node_head(object):
    def test_1(self, n):
        n.put_head(1)
        assert n.as_list() == [1]
        assert n.as_list(remove_nones=False) == [1] + [None] * 3
        
    def test_2(self, n):
        n.put_head(1)
        n.put_head(2)
        assert n.as_list() == [2, 1]
        assert n.as_list(remove_nones=False) == [2, 1] + [None] * 2
        
    def test_4(self, n):
        n.put_head(1)
        n.put_head(2)
        n.put_head(3)
        n.put_head(4)
        assert n.as_list() == [4, 3, 2, 1]
        assert n.as_list(remove_nones=False) == [4, 3, 2, 1]
        
    def test_full_node_error(self, n):
        with pytest.raises(IndexError) as excinfo:
            for i in range(5):
                n.put_head(i)
        assert 'node is full' in str(excinfo.value)
        
class Test_put_node_tail(object):
    def test_1(self, n):
        n.put_tail(1)
        assert n.as_list() == [1]
        assert n.as_list(remove_nones=False) == [1] + [None] * 3
        
    def test_2(self, n):
        n.put_tail(1)
        n.put_tail(2)
        assert n.as_list() == [1, 2]
        assert n.as_list(remove_nones=False) == [1, 2] + [None] * 2
        
    def test_4(self, n):
        n.put_tail(1)
        n.put_tail(2)
        n.put_tail(3)
        n.put_tail(4)
        assert n.as_list() == [1, 2, 3, 4]
        assert n.as_list(remove_nones=False) == [1, 2, 3, 4]
        
    def test_full_node_error(self, n):
        with pytest.raises(IndexError) as excinfo:
            for i in range(5):
                n.put_tail(i)
        assert 'node is full' in str(excinfo.value)
        
class Test_put_node_index(object):
    def test_1(self, n):
        n.put_index(1, 0)
        assert n.as_list() == [1]
        assert n.as_list(remove_nones=False) == [1] + [None] * 3
        
    def test_2(self, n):
        n.put_index(1, 0)
        n.put_index(2, 0)
        n.put_index(3, 0)
        assert n.as_list() == [3, 2, 1]
        assert n.as_list(remove_nones=False) == [3, 2, 1] + [None]
        
    def test_3(self, n):
        n.put_index(1, 0)
        n.put_index(2, 1)
        n.put_index(3, 2)
        assert n.as_list() == [1, 2, 3]
        assert n.as_list(remove_nones=False) == [1, 2, 3] + [None]
        
    def test_4_middle(self, n):
        n.put_index(1, 0)
        n.put_index(2, 1)
        n.put_index(3, 1)
        n.put_index(4, 2)
        assert n.as_list() == [1, 3, 4, 2]
        assert n.as_list(remove_nones=False) == [1, 3, 4, 2]
        
    def test_4_end(self, n):
        n.put_index(1, 0)
        n.put_index(2, 1)
        n.put_index(3, 1)
        n.put_index(4, 3)
        assert n.as_list() == [1, 3, 2, 4]
        assert n.as_list(remove_nones=False) == [1, 3, 2, 4]
        
    def test_full_node_error(self, n):
        with pytest.raises(IndexError) as excinfo:
            for i in range(5):
                n.put_index(i, i)
        assert 'node is full' in str(excinfo.value)
        
    def test_index_less_than_0(self, n):
        with pytest.raises(IndexError) as excinfo:
            n.put_index(1, -1)
        assert 'index must be >= 0' in str(excinfo.value)
        
    def test_index_greater_than_max_elements(self, n):
        with pytest.raises(IndexError) as excinfo:
            n.put_index(1, 4)
        assert 'index exceeds the number of maximum elements' in str(excinfo.value)
        
    def test_index_greater_than_num_elements(self, n):
        with pytest.raises(IndexError) as excinfo:
            n.put_index(1, 0)
            n.put_index(2, 1)
            n.put_index(3, 3)
        assert 'index exceeds number of elements in the node' in str(excinfo.value)
        
class Test_put_node_mixed(object):
    def test(self, n):
        n.put_tail(1)
        n.put_tail(2)
        n.put_head(3)
        assert n.as_list() == [3, 1, 2]
        assert n.as_list(remove_nones=False) == [3, 1, 2, None]
        
class Test_node_delete(object):
    def test_index_m1(self):
        with pytest.raises(IndexError) as excinfo:
            n = NodeUnrolled()
            n.delete(-1)
        assert 'index must be >= 0' in str(excinfo.value)
        
    def test_index_lone_element(self):
        n = NodeUnrolled()
        n.put_tail(1)
        n.delete(0)
        assert n.as_list() == []
        assert n.as_list(remove_nones=False) == [None, None, None, None]
        
    def test_index_0(self):
        n = NodeUnrolled()
        n.put_tail(1)
        n.put_tail(2)
        n.delete(0)
        assert n.as_list() == [2]
        assert n.as_list(remove_nones=False) == [2, None, None, None]
        
    def test_index_1(self):
        n = NodeUnrolled()
        n.put_tail(1)
        n.put_tail(2)
        n.delete(1)
        assert n.as_list() == [1]
        assert n.as_list(remove_nones=False) == [1, None, None, None]
        
    def test_index_1(self):
        n = NodeUnrolled()
        n.put_tail(1)
        n.put_tail(2)
        n.delete(1)
        assert n.as_list() == [1]
        assert n.as_list(remove_nones=False) == [1, None, None, None]
        
    def test_index_2(self):
        with pytest.raises(IndexError) as excinfo:
            n = NodeUnrolled()
            n.put_tail(1)
            n.put_tail(2)
            n.delete(2)
        assert 'index exceeds the number of elements' in str(excinfo.value)
        
    def test_index_head(self):
        n = NodeUnrolled()
        n.put_tail(1)
        n.put_tail(2)
        n.put_tail(3)
        n.put_tail(4)
        n.delete(0)
        assert n.as_list() == [2, 3, 4]
        assert n.as_list(remove_nones=False) == [2, 3, 4, None]
        
    def test_index_tail(self):
        n = NodeUnrolled()
        n.put_tail(1)
        n.put_tail(2)
        n.put_tail(3)
        n.put_tail(4)
        n.delete(3)
        assert n.as_list() == [1, 2, 3]
        assert n.as_list(remove_nones=False) == [1, 2, 3, None]

#####
# LinkedListUnrolled
#

@pytest.fixture()
def l():
    l = LinkedListUnrolled()
    return l

class Test_create_LinkedListUnrolled(object):
    def test_type(self, l):
        assert isinstance(l, LinkedListUnrolled)
        
    def test_get_head(self, l):
        assert l.get_head() is None
        
    def test_get_tail(self, l):
        assert l.get_tail() is None
        
    def test_get_index(self, l):
        assert l.get_index(0) is None
        
    def test_get_length(self, l):
        assert l.get_length() == 0
        
    def test_as_list(self, l):
        assert l.as_list() == []

@pytest.fixture()
def l_single():
    l = LinkedListUnrolled()
    l.put_tail(1)
    l.put_tail(2)
    return l

@pytest.fixture()
def l_multiple():
    l = LinkedListUnrolled()
    l.add_node_tail()
    l.put_tail(1)
    l.add_node_tail()
    l.put_tail(2)
    l.put_tail(3)
    l.add_node_tail()
    l.put_tail(4)
    return l

class Test_get_head_and_tail(object):
    def test_get_head_single(self, l_single):
        assert l_single.get_head() == 1
        
    def test_get_tail_single(self, l_single):
        assert l_single.get_tail() == 2
        
    def test_get_head_multiple(self, l_multiple):
        assert l_multiple.get_head() == 1
        
    def test_get_tail_multiple(self, l_multiple):
        assert l_multiple.get_tail() == 4

class Test_get_index(object):
    def test_get_index_m1_single(self, l_single):
        with pytest.raises(IndexError) as excinfo:
            l_single.get_index(-1)
        assert 'index must be >= 0' in str(excinfo.value)
        
    def test_get_index_0_single(self, l_single):
        assert l_single.get_index(0) == 1
        
    def test_get_index_1_single(self, l_single):
        assert l_single.get_index(1) == 2
        
    def test_get_index_2_single(self, l_single):
        with pytest.raises(IndexError) as excinfo:
            l_single.get_index(2)
        assert 'index exceeds list length' in str(excinfo.value)
        
    def test_get_index_m1_multiple(self, l_multiple):
        with pytest.raises(IndexError) as excinfo:
            l_multiple.get_index(-1)
        assert 'index must be >= 0' in str(excinfo.value)
        
    def test_get_index_0_multiple(self, l_multiple):
        assert l_multiple.get_index(0) == 1
        
    def test_get_index_1_multiple(self, l_multiple):
        assert l_multiple.get_index(1) == 2
        
    def test_get_index_2_multiple(self, l_multiple):
        assert l_multiple.get_index(2) == 3
        
    def test_get_index_3_multiple(self, l_multiple):
        assert l_multiple.get_index(3) == 4
        
    def test_get_index_4_multiple(self, l_multiple):
        with pytest.raises(IndexError) as excinfo:
            l_multiple.get_index(4)
        assert 'index exceeds list length' in str(excinfo.value)
        
    def test_get_index_empty_first_node(self, l_multiple):
        l = LinkedListUnrolled()
        l.add_node_tail()
        l.add_node_tail()
        l.put_tail(1)
        assert l.get_index(0) == 1
        
    def test_get_index_empty_second_node(self, l_multiple):
        l = LinkedListUnrolled()
        l.add_node_tail()
        l.put_tail(1)
        l.add_node_tail()
        l.add_node_tail()
        l.put_tail(2)
        assert l.get_index(0) == 1
        assert l.get_index(1) == 2

class Test_get_length(object):
    def test_single(self, l_single):
        assert l_single.get_length() == 2
        
    def test_multiple(self, l_multiple):
        assert l_multiple.get_length() == 4

class Test_as_list(object):
    def test_single(self, l_single):
        assert l_single.as_list() == [1, 2]
        assert l_single.as_list(nested=True) == [[1, 2]]
        assert l_single.as_list(remove_nones = False) == [1, 2, None, None]
        assert l_single.as_list(nested=True, remove_nones=False) == [[1, 2, None, None]]
        
    def test_multiple(self, l_multiple):
        assert l_multiple.as_list() == [1, 2, 3, 4]
        assert l_multiple.as_list(nested=True) == [[1], [2, 3], [4]]
        assert l_multiple.as_list(remove_nones = False) == [1, None, None, None,
                                                            2,    3, None, None,
                                                            4, None, None, None]
        assert l_multiple.as_list(nested=True, remove_nones=False) == [[1, None, None, None],
                                                                       [2,    3, None, None],
                                                                       [4, None, None, None]]

#####
# Put methods
#

def test_all_head():
    l = LinkedListUnrolled()
    l.put_head(1)
    l.put_head(2)
    l.put_head(3)
    l.put_head(4)
    l.put_head(5)
    assert l.as_list() == [5, 4, 3, 2, 1]
    assert l.as_list(nested=True) == [[5, 4, 3, 2], [1]]

def test_all_tail():
    l = LinkedListUnrolled()
    l.put_tail(1)
    l.put_tail(2)
    l.put_tail(3)
    l.put_tail(4)
    l.put_tail(5)
    assert l.as_list() == [1, 2, 3, 4, 5]
    assert l.as_list(nested=True) == [[1, 2, 3, 4], [5]]

def test_mix_head_tail():
    l = LinkedListUnrolled()
    l.put_head(1)
    l.put_tail(2)
    l.put_head(3)
    l.put_tail(4)
    l.put_head(5)
    assert l.as_list() == [5, 3, 1, 2, 4]
    assert l.as_list(nested=True) == [[5, 3, 1, 2], [4]]
    
class Test_list_put_index_single(object):            
    def test_empty(self):
        l = LinkedListUnrolled()
        l.put_index(1, index=0)
        assert l.as_list() == [1]
        assert l.as_list(nested=True) == [[1]]
    
    def test_m1(self, l_single):
        with pytest.raises(IndexError) as excinfo:
            l_single.put_index(3, index=-1)
        assert 'index must be >= 0' in str(excinfo.value)
    
    def test_0(self, l_single):
        l_single.put_index(3, index=0)
        assert l_single.as_list() == [3, 1, 2]
        assert l_single.as_list(nested=True) == [[3, 1, 2]]
    
    def test_1(self, l_single):
        l_single.put_index(3, index=1)
        assert l_single.as_list() == [1, 3, 2]
        assert l_single.as_list(nested=True) == [[1, 3, 2]]
    
    def test_2(self, l_single):
        l_single.put_index(3, index=2)
        assert l_single.as_list() == [1, 2, 3]
        assert l_single.as_list(nested=True) == [[1, 2, 3]]
    
    def test_3(self, l_single):
        with pytest.raises(IndexError) as excinfo:
            l_single.put_index(3, index=3)
        assert 'index exceeds list length' in str(excinfo.value)
    
    def test_overflow_create_new_node(self, l_single):
        l_single.put_index(3, index=2)
        l_single.put_index(4, index=3)
        l_single.put_index(5, index=4)
        assert l_single.as_list() == [1, 2, 3, 4, 5]
        assert l_single.as_list(nested=True) == [[1, 2, 3, 4], [5]]
    
class Test_list_put_index_multiple(object):    
    def test_m1(self, l_multiple):
        with pytest.raises(IndexError) as excinfo:
            l_multiple.put_index(3, index=-1)
        assert 'index must be >= 0' in str(excinfo.value)
    
    def test_0(self, l_multiple):
        l_multiple.put_index(0, index=0)
        assert l_multiple.as_list() == [0, 1, 2, 3, 4]
        assert l_multiple.as_list(nested=True) == [[0, 1], [2, 3], [4]]
    
    def test_1(self, l_multiple):
        l_multiple.put_index(0, index=1)
        assert l_multiple.as_list() == [1, 0, 2, 3, 4]
        assert l_multiple.as_list(nested=True) == [[1, 0], [2, 3], [4]]
    
    def test_1_2x(self, l_multiple):
        l_multiple.put_index(0, index=1)
        l_multiple.put_index(-1, index=1)
        assert l_multiple.as_list() == [1, -1, 0, 2, 3, 4]
        assert l_multiple.as_list(nested=True) == [[1, -1, 0], [2, 3], [4]]
    
    def test_2(self, l_multiple):
        l_multiple.put_index(0, index=2)
        assert l_multiple.as_list() == [1, 2, 0, 3, 4]
        assert l_multiple.as_list(nested=True) == [[1], [2, 0, 3], [4]]
    
    def test_3(self, l_multiple):
        l_multiple.put_index(0, index=3)
        assert l_multiple.as_list() == [1, 2, 3, 0, 4]
        assert l_multiple.as_list(nested=True) == [[1], [2, 3, 0], [4]]
    
    def test_4(self, l_multiple):
        l_multiple.put_index(0, index=4)
        assert l_multiple.as_list() == [1, 2, 3, 4, 0]
        assert l_multiple.as_list(nested=True) == [[1], [2, 3], [4, 0]]
    
    def test_5(self, l_multiple):
        with pytest.raises(IndexError) as excinfo:
            l_multiple.put_index(3, index=5)
        assert 'index exceeds list length' in str(excinfo.value)
    
    def test_overflow_1(self, l_multiple):
        l_multiple.put_index(0, index=1)
        l_multiple.put_index(-1, index=1)
        l_multiple.put_index(-2, index=1)
        l_multiple.put_index(-3, index=1)
        assert l_multiple.as_list() == [1, -3, -2, -1, 0, 2, 3, 4]
        assert l_multiple.as_list(nested=True) == [[1, -3, -2, -1], [0, 2, 3], [4]]
    
    def test_overflow_1_2x(self, l_multiple):
        l_multiple.put_index(0, index=1)
        l_multiple.put_index(-1, index=1)
        l_multiple.put_index(-2, index=1)
        l_multiple.put_index(-3, index=1)
        l_multiple.put_index(-4, index=1)
        l_multiple.put_index(-5, index=1)
        assert l_multiple.as_list() == [1, -5, -4, -3, -2, -1, 0, 2, 3, 4]
        assert l_multiple.as_list(nested=True) == [[1, -5, -4, -3], [-2, -1, 0, 2], [3, 4]]
    
    def test_overflow_1_3x(self, l_multiple):
        l_multiple.put_index(0, index=1)
        l_multiple.put_index(-1, index=1)
        l_multiple.put_index(-2, index=1)
        l_multiple.put_index(-3, index=1)
        l_multiple.put_index(-4, index=1)
        l_multiple.put_index(-5, index=1)
        l_multiple.put_index(-6, index=1)
        l_multiple.put_index(-7, index=1)
        l_multiple.put_index(-8, index=1)
        assert l_multiple.as_list() == [1, -8, -7, -6, -5, -4, -3, -2, -1, 0, 2, 3, 4]
        assert l_multiple.as_list(nested=True) == [[1,-8, -7, -6], [-5, -4, -3, -2], [-1, 0, 2, 3], [4]]
    
    def test_overflow_incremental_1(self, l_multiple):
        l_multiple.put_index(0, index=1)
        l_multiple.put_index(-1, index=2)
        l_multiple.put_index(-2, index=3)
        l_multiple.put_index(-3, index=4)
        assert l_multiple.as_list() == [1, 0, -1, -2, -3, 2, 3, 4]
        assert l_multiple.as_list(nested=True) == [[1, 0, -1, -2], [-3, 2, 3], [4]]
    
    def test_overflow_incremental_2(self, l_multiple):
        l_multiple.put_index(0, index=1)
        l_multiple.put_index(-1, index=2)
        l_multiple.put_index(-2, index=3)
        l_multiple.put_index(-3, index=4)
        l_multiple.put_index(-4, index=5)
        l_multiple.put_index(-5, index=6)
        assert l_multiple.as_list() == [1, 0, -1, -2, -3, -4, -5, 2, 3, 4]
        assert l_multiple.as_list(nested=True) == [[1, 0, -1, -2], [-3, -4, -5, 2], [3, 4]]
    
    def test_overflow_incremental_3(self, l_multiple):
        l_multiple.put_index(0, index=1)
        l_multiple.put_index(-1, index=2)
        l_multiple.put_index(-2, index=3)
        l_multiple.put_index(-3, index=4)
        l_multiple.put_index(-4, index=5)
        l_multiple.put_index(-5, index=6)
        l_multiple.put_index(-6, index=7)
        l_multiple.put_index(-7, index=8)
        l_multiple.put_index(-8, index=9)
        assert l_multiple.as_list() == [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, 2, 3, 4]
        assert l_multiple.as_list(nested=True) == [[1, 0, -1, -2], [-3, -4, -5, -6], [-7, -8, 2, 3], [4]]

#####
# Search
#

def test_search_empty_list():
    l = LinkedListUnrolled()
    assert l.search(1) == []

class Test_search_single(object):
    def test_no_matches(self, l_single):
        assert l_single.search(0) == []

    def test_one_match(self, l_single):
        assert l_single.search(1) == [0]
        assert l_single.search(2) == [1]

    def test_multiple_matches(self):
        l = LinkedListUnrolled()
        l.put_head(1)
        l.put_head(2)
        l.put_head(1)
        l.put_head(3)
        l.put_head(1)
        assert l.search(1) == [0, 2, 4]

class Test_search_multiple(object):
    def test_no_matches(self, l_multiple):
        assert l_multiple.search(0) == []

    def test_one_match(self, l_multiple):
        assert l_multiple.search(1) == [0]
        assert l_multiple.search(2) == [1]
        assert l_multiple.search(3) == [2]
        assert l_multiple.search(4) == [3]

    def test_multiple_matches(self):
        l = LinkedListUnrolled()
        l.add_node_tail()
        l.put_tail(1)
        l.add_node_tail()
        l.put_tail(2)
        l.put_tail(1)
        l.put_tail(3)
        l.add_node_tail()
        l.put_tail(4)
        l.add_node_tail()
        l.put_tail(1)
        assert l.search(1) == [0, 2, 5]

#####
# Delete
#

def test_delete_index_empty():
    with pytest.raises(ValueError) as excinfo:
        l = LinkedListUnrolled()
        l.delete(0)
    assert 'list is empty' in str(excinfo.value)

def test_delete_index_m1():
    with pytest.raises(IndexError) as excinfo:
        l = LinkedListUnrolled()
        l.put_tail(1)
        l.put_tail(2)
        l.delete(-1)
    assert 'index must be >= 0' in str(excinfo.value)

def test_delete_index_gt_length():
    with pytest.raises(IndexError) as excinfo:
        l = LinkedListUnrolled()
        l.put_tail(1)
        l.put_tail(2)
        l.delete(5)
    assert 'index exceeds list length' in str(excinfo.value)

class Test_delete_index_single(object):                
    def test_0(self, l_single):
        l_single.delete(0)
        assert l_single.as_list() == [2]
        assert l_single.as_list(nested=True) == [[2]]
    
    def test_1(self, l_single):
        l_single.delete(1)
        assert l_single.as_list() == [1]
        assert l_single.as_list(nested=True) == [[1]]

class Test_delete_index_multiple(object):                
    def test_0(self, l_multiple):
        l_multiple.delete(0)
        assert l_multiple.as_list() == [2, 3, 4]
        assert l_multiple.as_list(nested=True) == [[], [2, 3], [4]]
    
    def test_1(self, l_multiple):
        l_multiple.delete(1)
        assert l_multiple.as_list() == [1, 3, 4]
        assert l_multiple.as_list(nested=True) == [[1], [3], [4]]
    
    def test_2(self, l_multiple):
        l_multiple.delete(2)
        assert l_multiple.as_list() == [1, 2, 4]
        assert l_multiple.as_list(nested=True) == [[1], [2], [4]]
    
    def test_3(self, l_multiple):
        l_multiple.delete(3)
        assert l_multiple.as_list() == [1, 2, 3]
        assert l_multiple.as_list(nested=True) == [[1], [2, 3], []]
    
    def test_multiple(self, l_multiple):
        l_multiple.delete(0)
        l_multiple.delete(1)
        assert l_multiple.as_list() == [2, 4]
        assert l_multiple.as_list(nested=True) == [[], [2], [4]]
    
    def test_all_empty_nodes_plus_one(self, l_multiple):
        with pytest.raises(ValueError) as excinfo:
            l_multiple.delete(0)
            l_multiple.delete(0)
            l_multiple.delete(0)
            l_multiple.delete(0)
            l_multiple.delete(0)
        assert 'list is empty' in str(excinfo.value)

