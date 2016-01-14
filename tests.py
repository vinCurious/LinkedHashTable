""" 
file: tests.py
description: Verify the LinkedHashTable class implementation
author: vinay more
"""

from linkedhashtable import LinkedHashTable

def print_set( a_set ):
    for word in a_set: # uses the iter method
        print( word, end=" " )
    print()

def test0():
    """ already provided test for adding, printing and removing elements
     """
    print("-----------------------TEST0 START-----------------------")
    table = LinkedHashTable( 100 )
    table.add( "to" )
    table.add( "do" )
    table.add( "is" )
    table.add( "to" )
    table.add( "be" )

    print_set( table )

    #
    print( "'to' in table?", table.contains( "to" ) )
    table.remove( "to" )
    print( "'to' in table?", table.contains( "to" ) )

    print_set( table )
    print("-----------------------TEST0 END-----------------------")

def test1():
    """
    This method tests removing of front, middle and back element
    """
    print("-----------------------TEST1 START-----------------------")
    table1 = LinkedHashTable(4)
    table1.add( "to" )
    table1.add( "be" )
    table1.add( "or" )
    table1.add( "not" )
    table1.add( "to1" )
    table1.add( "be1" )

    print("Hash Table: ")
    print_set(table1)
    print( "\n'to' in table?", table1.contains( "to" ) )
    print( "Removing front i.e. 'to'", )
    table1.remove("to")
    print( "'to' in table?", table1.contains( "to" ) )
    print("Hash Table: ")
    print_set(table1)

    print( "\n'not' in table?", table1.contains( "not" ) )
    table1.remove( "not" )
    print( "Removing middle elemtnt i.e 'not'", )
    print( "'not' in table?", table1.contains( "not" ) )
    print("Hash Table: ")
    print_set(table1)

    print( "\n'be1' in table?", table1.contains( "be1" ) )
    table1.remove( "be1" )
    print( "Removing last elemtnt i.e 'be1'", )
    print( "'be1' in table?", table1.contains( "be1" ) )
    print("Hash Table: ")
    print_set(table1)
    print("-----------------------TEST1 END-----------------------")

def test2():
    """
        This method tests for adding duplicate elements and testing remove method for non-existing elements
        """
    print("-----------------------TEST2 START-----------------------")
    table2 = LinkedHashTable(4)
    table2.add( "to" )
    table2.add( "be" )
    table2.add( "or" )
    table2.add( "not" )
    table2.add( "to1" )
    table2.add( "be1" )

    print("\nHash Table: ")
    print_set( table2 )
    print( "adding duplicate 'to1'")
    table2.add("to1")
    print("Hash Table: ")
    print_set(table2)

    print("\nHash Table: ")
    print_set( table2 )
    print( "removing non-existing element 'here'")
    table2.remove("here")
    print("Hash Table: ")
    print_set(table2)
    print("-----------------------TEST2 END-----------------------")

def test3():
    """
        This method tests for rehashing and downsizing scenarios
        """
    print("-----------------------TEST3 START-----------------------")
    table3 = LinkedHashTable(12)
    table3.add( "to" )
    table3.add( "be" )
    table3.add( "or" )
    table3.add( "not" )
    table3.add( "to1" )
    table3.add( "be1" )
    table3.add( "to2" )
    table3.add( "be2" )

    print("\nHash Table: ")
    print_set( table3 )

    print("Testing whether the table increases when loadlimit is reached by adding 'here'")
    table3.add( "here" )
    print("\nHash Table: ")
    print_set( table3 )

    print("Testing whether the table downsizes when size goes below loadlimit by removing element 'here'")
    table3.remove("here")


    print("\nHash Table: ")
    print_set(table3)

    print("-----------------------TEST3 END-----------------------")

if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
