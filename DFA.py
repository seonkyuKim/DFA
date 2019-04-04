# Function that acts like DFA
# Return Ture if it accepts input value.
# If not, return False.
def DFA(input):
    """
    - internal states : q0, q1, q2, q3, q4
    - input alphabet : {0, 1}
    - transition function :
    (q0, 0) = q0  /  (q0, 1) = q1
    (q1, 0) = q2  /  (q1, 1) = q3
    (q2, 0) = q4  /  (q2, 1) = q0
    (q3, 0) = q1  /  (q3, 1) = q2
    (q4, 0) = q3  /  (q4, 1) = q4
    - initial state : q0
    - final state : q0
    """

    q0 = 'q0'
    q1 = 'q1'
    q2 = 'q2'
    q3 = 'q3'
    q4 = 'q4'

    curr_state = q0

    iuput_list = [char for char in input]

    for element in iuput_list:
        
        if curr_state == q0:
            if element == '0':
                curr_state = q0
            elif element == '1':
                curr_state = q1
            continue

        if curr_state == q1:
            if element == '0':
                curr_state = q2
            elif element == '1':
                curr_state = q3
            continue

        if curr_state == q2:
            if element == '0':
                curr_state = q4
            elif element == '1':
                curr_state = q0
            continue

        if curr_state == q3:
            if element == '0':
                curr_state = q1
            elif element == '1':
                curr_state = q2
            continue

        if curr_state == q4:
            if element == '0':
                curr_state = q3
            elif element == '1':
                curr_state = q4
            continue

    if curr_state == q0:
        return True
    else:
        return False


# Function that returns False if the input is not binary value.
# Reference : https://www.geeksforgeeks.org/python-check-if-a-given-string-is-binary-string-or-not/
def checkBinary(input):
  
    # set function convert string into set of characters . 
    p = set(input) 
  
    # declare set of '0', '1' . 
    s = {'0', '1'} 
  
    # check set p is same as set s 
    # or set p contains only '0' 
    # or set p contains only '1' 
    # or not, if any one conditon 
    # is true then string is accepted 
    # otherwise not . 
    if s == p or p == {'0'} or p == {'1'}: 
        return True
    else : 
        return False

description = \
"""Input binary value of 0 and 1.
If you want to exit program, input 'exit'.
"""

# Main fucntion.
# Get the input from user and print if it is accepted or not.
if __name__ == "__main__" :
    
    while True:
        n = input(description)
        if n == 'exit':
            break
        if checkBinary(n) == False:
            print('Error: Input value is not binary.', end='\n')
            continue
        
        is_accept = DFA(n)

        if is_accept == True:
            print('Accept\n')
        else:
            print('Not accept\n')
        

    