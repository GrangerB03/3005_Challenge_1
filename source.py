#Authour: Ben Granger
#Student #101221725
#Carleton University - COMP 3005 W24 - Challenge 1

#relation class, stores all of the necessary data about a relation

from relation import relation
import queries as q

relations = []
    
def main():
    while 1:
        file_name = input("Please input the file with your query here (q to quit): ")
        if(file_name == 'q'):
            break
        try:
            file = open(file_name, "r")
        except:
            print(file_name + " does not exist.")
            continue
        #content is char array
        content = file.read()
        word_arr = split_into_words(content)
        relations = get_relations_data(word_arr)
        get_queries(word_arr)
        #debugging for later:
        #print("\nStored relations:\n")
        #for i in range(len(relations)):
           #relations[i].print()
        #print(word_arr)
        relations = []
        
#separate into words
def split_into_words(args: str):
    count = 0
    word_count = 0
    string_list = [""]
    while(count < len(args)):
        if(args[count] != " " and args[count] != '\n'):
            string_list[word_count] += args[count]
        else:
            word_count += 1
            string_list.append("")
        count += 1
    return string_list
    
#separate into syntax
#key characters/phrases:
#'{}' for relations
#convert relations to data structures

#known limitation: there cannot be an element such as 'Billy Joel,' as the name, they must
#not have a space in the element
def get_relations_data(args: str):
    #RELATIONS:
    #find all instances of '{'
    #first '(' before that signifies the name of the relation to the leftjoin
    #inbetween these brackets are the column names
    #after the '{' and before the '}' are the rows, row is ended by a '\n'
    #in this loop:
    #i stores the start of the rows
    #l stores the end of the rows
    #j stores the start of the column names
    #k stores the end of the column names
    for i in range(len(args)):
        if(args[i] == '{'):
            num_cols = 0
            tmp = relation()
            #walk backwards until we find a '('
            for j in range(i, 0, -1):
                if(args[j][0] == '('):
                    #found, string before is relation name
                    tmp.set_name(args[j-1])
                    #we need to find columns now
                    columns = []
                    first_col = args[j]
                    columns.append(first_col[1:-1])
                    #check for case of one columnn
                    if(first_col[len(first_col) - 1] != ')'):
                        #loop until we find a ')' at the end of a column name
                        for k in range(j + 1, len(args), 1):
                            #add the name minus the comma (last char)
                            columns.append(args[k][:-1])
                            #if there's a ')' at the end of last name, end loop
                            if(args[k][len(args[k]) - 1] == ')'):
                                break
                    tmp.set_columns(columns)
                    num_cols = len(columns)
                    break
            #now we get the rows
            #first, get end of rows
            counter = 0
            row = []
            #loop over all row elements
            for l in range(i + 1, len(args)):
                #if we reach end, break
                if(args[l] == '}'):
                    break
                #add row, if there is comma at end of string remove it
                if(args[l][len(args[l]) - 1] == ','):
                    row.append(args[l][:-1])
                else:
                    row.append(args[l])
                #increment counter
                counter +=  1
                #we know we've reached the end of a row if counter % num_cols = 0
                if(counter % num_cols == 0):
                    tmp.add_row(row)
                    row = []
            #add the temp object to the list
            relations.append(tmp)
                    
            
    print("\nThe following relations were found: \n")
    for i in range(len(relations)):
        relations[i].print()
        print("\n")
    return relations

#we have relations in data structures, now let's get the queries sorted into functions
#select, proj, cartesian, innerjoin, outerjoin, union, intersection, minus
#to solve the nesting issue, we will provide the option to store a query and reference it by name later
#do this with the following syntax: NAME = QUERY
#this will change the stored name to be designated name
def get_queries(args: str):
    #loop over input
    for i in range(len(args)):
        #we already have a list of words as the args
        #check for special keywords as said above
        #note for these functions, they will not check for correctness
        #must check to make sure that the query is a real query and that the keyword isn't in a
        #relation, this is case sensitive
        match args[i]:
            case "select":
                print("selection query found\n")
                result = q.selection(args, i, relations)
                if(not result == None):
                    result.print()
                    if(args[i-1] == "="):
                        result.set_name(args[i-2])
                    relations.append(result)
                    result = None
                    print()
                else:
                    print("Invalid selection query found")
            case "proj":
                print("projection query found")
                result = q.projection(args, i, relations)
                if(not result == None):
                    result.print()
                    if(args[i-1] == "="):
                        result.set_name(args[i-2])
                    relations.append(result)
                    result = None
                    print()
                else:
                    print("Invalid projection query found")
            case "cartesian":
                print("cartesian product query found")
                result = q.cartesian_product(args, i, relations)
                if(not result == None):
                    result.print()
                    if(args[i-1] == "="):
                        result.set_name(args[i-2])
                    relations.append(result)
                    result = None
                    print()
                else:
                    print("Invalid cartesian product query found - no return")
            case "innerjoin":
                print("innerjoin query found")
                result = q.inner_join(args, i, relations)
                if(not result == None):
                    result.print()
                    if(args[i-1] == "="):
                        result.set_name(args[i-2])
                    relations.append(result)
                    result = None
                    print()
                else:
                    print("Invalid inner join query found")
            case "outerjoin":
                print("outer join query found")
                result = q.outer_join(args, i, relations)
                if(not result == None):
                    result.print()
                    if(args[i-1] == "="):
                        result.set_name(args[i-2])
                    relations.append(result)
                    result = None
                    print()
                else:
                    print("Invalid outer join query found")
            case "union":
                print("union query found")
                result = q.union(args, i, relations)
                if(not result == None):
                    result.print()
                    if(args[i-1] == "="):
                        result.set_name(args[i-2])
                    relations.append(result)
                    result = None
                    print()
                else:
                    print("Invalid union query found")
            case "intersect":
                print("intersection query found")
                result = q.intersection(args, i, relations)
                if(not result == None):
                    result.print()
                    if(args[i-1] == "="):
                        result.set_name(args[i-2])
                    relations.append(result)
                    result = None
                    print()
                else:
                    print("Invalid intersection query found")
            case "minus":
                print("minus query found")
                result = q.minus(args, i, relations)
                if(not result == None):
                    result.print()
                    if(args[i-1] == "="):
                        result.set_name(args[i-2])
                    relations.append(result)
                    result = None
                    print()
                else:
                    print("Invalid minus query found")


#perform query operations on data structures
#return result of query operations to user, repeat loop
    
main()