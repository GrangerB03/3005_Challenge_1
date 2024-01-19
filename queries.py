#query functions:
from relation import relation

#syntax: select Col<OPERATOR><VALUE>(RELATION)
def selection(args: str, location: int, relations):
    if location == len(args):
        print("Invalid selection query found")
        return
    operand = args[location+1]
    operators = ["=", ">", "<"]
    operator_location = -1
    operator_id = -1
    relation_start = -1
    relation_end = -1
    #find operator
    for i in range(len(operators)):
        if(operators[i] in operand):
            operator_id = i
            for j in range(len(operand)):
                if(operand[j] == operators[operator_id]):
                    operator_location = j
                    break
            break
            
    #get operands of operator
    lefthand = operand[:operator_location]
    righthand = ""
    for i in range(operator_location, len(operand)):
        if(operand[i] == '('):
            righthand = operand[operator_location + 1:i]
            relation_start = i
    
    #now, we have operands and operator, just need relation
    #get end bracket location
    for i in range(relation_start, len(operand)):
        if(operand[i] == ')'):
            relation_end = i
            break
    
    #error check
    if(operator_location == -1 or operator_id == -1 or relation_start == -1 or relation_end == -1):
        print("Invalid query - syntax error at string " + args[location + 1])
        return 1
    relation_name = operand[relation_start + 1: relation_end]
    relation = None
    for i in range(len(relations)):
        if(relations[i].get_name() == relation_name):
            relation = relations[i]
    #now we have all the pieces, let's put it together
    return relation.select(lefthand, operators[operator_id], righthand)
    
    
#syntax: 'proj col1 col2 ... (Relation)'
#spaces are required    
def projection(args: str, location: int, relations):
    if location == len(args):
        print("Invalid projection query found")
        return
    columns = []
    counter = location + 1
    while(not '(' in args[counter]):
        columns.append(args[counter])
        counter += 1
    #counter stores the string with the relation now
    relation_name = args[counter][1:len(args[counter]) - 1]
    #we have all of the required elements
    relation = None
    for i in range(len(relations)):
        if(relations[i].get_name() == relation_name):
            relation = relations[i]
    if(relation == None):
        print("Invalid projection query found")
    return relation.project(columns)
    
#syntax: RELATION cartesian RELATION
def cartesian_product(args: str, location: int, relations):
    if(location == len(args)):
        print("Invalid cartesian product query found")
        return
    left = -1
    right = -1
    for i in range(len(relations)):
        #check left
        if(args[location-1] == relations[i].get_name()):
            left = relations[i]
        #check right
        if(args[location+1] == relations[i].get_name()):
            right = relations[i]
    
    #we now either have both relations or one or both wasn't found
    if(left == -1 or right == -1):
        print("Invalid cartesian product query found")
        return
    return relation.cartesian(left, right)
   
#syntax: lefthand innerjoin (Col1=Col2) righthand   
def inner_join(args: str, location: int, relations):
    if(not location + 2 <= len(args)):
        print("Invalid inner join query found")
        return
    left = -1
    right = -1
    for i in range(len(relations)):
        #check left
        if(args[location-1] == relations[i].get_name()):
            left = relations[i]
        #check right
        if(args[location+2] == relations[i].get_name()):
            right = relations[i]
    #we now either have both relations or one or both wasn't found
    if(left == -1 or right == -1):
        print("Invalid inner join query found")
        return
    return relation.inner_join(left, right, args[location + 1])

#syntax: lefthand outerjoin (Col1=Col2) righthand
def outer_join(args: str, location: int, relations):
    if(not location + 2 <= len(args)):
        print("Invalid outer join query found")
        return
    left = -1
    right = -1
    for i in range(len(relations)):
        #check left
        if(args[location-1] == relations[i].get_name()):
            left = relations[i]
        #check right
        if(args[location+2] == relations[i].get_name()):
            right = relations[i]
    #we now either have both relations or one or both wasn't found
    if(left == -1 or right == -1):
        print("Invalid outer join query found")
        return
    return relation.outer_join(left, right, args[location + 1])

#syntax: lefthand union righthand
def union(args: str, location: int, relations):
    if(location == len(args)):
        print("Invalid union query found")
        return
    left = -1
    right = -1
    for i in range(len(relations)):
        #check left
        if(args[location-1] == relations[i].get_name()):
            left = relations[i]
        #check right
        if(args[location+1] == relations[i].get_name()):
            right = relations[i]
    
    #we now either have both relations or one or both wasn't found
    if(left == -1 or right == -1):
        print("Invalid union query found")
        return
    return relation.union(left, right)

#syntax: lefthand intersect righthand
def intersection(args: str, location: int, relations):
    if(location == len(args)):
        print("Invalid intersection query found")
        return
    left = -1
    right = -1
    for i in range(len(relations)):
        #check left
        if(args[location-1] == relations[i].get_name()):
            left = relations[i]
        #check right
        if(args[location+1] == relations[i].get_name()):
            right = relations[i]
    
    #we now either have both relations or one or both wasn't found
    if(left == -1 or right == -1):
        print("Invalid intersection query found")
        return
    return relation.intersect(left, right)

#syntax: lefthand minus righthand
def minus(args: str, location: int, relations):
    if(location == len(args)):
        print("Invalid minus query found")
        return
    left = -1
    right = -1
    for i in range(len(relations)):
        #check left
        if(args[location-1] == relations[i].get_name()):
            left = relations[i]
        #check right
        if(args[location+1] == relations[i].get_name()):
            right = relations[i]
    
    #we now either have both relations or one or both wasn't found
    if(left == -1 or right == -1):
        print("Invalid minus query found")
        return
    return relation.subtract(left, right)
