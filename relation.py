class relation:
    def __init__(self):
        self.name = ""
        self.columns = []
        self.rows = []
        
    def set_name(self, n):
        self.name = n
        
    def set_columns(self, cols):
        self.columns = cols
        
    def set_rows(self, rws):
        self.rows = rws
        
    def add_row(self, row):
        self.rows.append(row)
    
    def get_name(self):
        return self.name

    def get_column_names(self):
        return self.columns
        
    def get_row(self, i):
        if(i >= len(self.rows)):
            return None
        return self.rows[i]
    
    def get_rows(self):
        return self.rows
    
    def get_column(self, name):
        if(name in self.columns):
            data = []
            column_num = -1
            for i in range(len(self.columns)):
                if(name == self.columns[i]):
                    column_num = i
            for i in range(len(self.rows)):
                #print("getting column " + str(column_num) + " from row " + str(self.rows[i]))
                data.append(self.rows[i][column_num])
            return data
        return None

    def print(self):
        print("Name: " + self.name)
        print("Columns: " + str(self.columns))
        for i in range(len(self.rows)):
            print("         " + str(self.rows[i]))
        print("\n")
    
    def select(self, lefthand, operator, righthand):
        #check if column exists
        if(not lefthand in self.columns):
            return None
        #make relation
        data = relation()
        data.set_name("Result of selection query: " + lefthand + operator + righthand + " on relation " + self.name)
        data.set_columns(self.columns)
        flag = False
        #check if float conversion needed
        if(righthand.isdigit()):
            righthand = float(righthand)
            flag = True
        #loop over columns
        for i in range(len(self.columns)):
            #found column, i is location
            if(self.columns[i] == lefthand):
                #three cases for each operator
                #each case, loop over all rows, then check if float conversion happened
                #if so, we convert element to float, else just compare,
                #if comparison is true, add row to output
                match operator:
                    case "=":
                        for row in range(len(self.rows)):
                            #print("checking if " + self.rows[row][i] + operator + str(righthand) + " " + str(self.rows[row][i] == righthand))
                            if(flag):
                                if(not self.rows[row][i].isdigit()):
                                    return None
                                element = float(self.rows[row][i])
                                if(element == righthand):
                                    data.add_row(self.rows[row])
                            else:
                                if(self.rows[row][i] == righthand):
                                    data.add_row(self.rows[row])
                    case ">":
                        for row in range(len(self.rows)):
                           #print("checking if " + self.rows[row][i] + operator + str(righthand) + " " + str(self.rows[row][i] > righthand))
                            if(flag):
                                if(not self.rows[row][i].isdigit()):
                                    return None
                                element = float(self.rows[row][i])
                                if(element > righthand):
                                    data.add_row(self.rows[row])
                            else:
                                if(self.rows[row][i] > righthand):
                                    data.add_row(self.rows[row])
                    case "<":
                       for row in range(len(self.rows)):
                            #print("checking if " + self.rows[row][i] + operator + str(righthand) + " " + str(self.rows[row][i] < righthand))
                            if(flag):
                                if(not self.rows[row][i].isdigit()):
                                    return None
                                element = float(self.rows[row][i])
                                if(element < righthand):
                                    data.add_row(self.rows[row])
                            else:
                                if(self.rows[row][i] < righthand):
                                    data.add_row(self.rows[row])
        return data

    def column_join_operation(self, left_col, right_col):
        #check if columns exist
        if(not left_col in self.columns and not right_col in self.columns):
            return None
        #make relation
        data = relation()
        data.set_columns(self.columns)
        left_index = -1
        right_index = -1
        #get column indecies
        for i in range(len(self.columns)):
            if(left_col == self.columns[i]):
                left_index = i
            if(right_col == self.columns[i]):
                right_index = i
        #loop over rows
        for i in range(len(self.rows)):
            #check if row has identical columns at indecies
            if(self.rows[i][left_index] == self.rows[i][right_index]):
                #if so add row
                data.add_row(self.rows[i])
        return data
        
    def project(self, cols):
        x = []
        #error checking, I'm sure there's a way to do it in the second loop but I'm tired
        for i in range(len(cols)):
            if(not cols[i] in self.columns):
                print("Invalid projection query found")
        for i in range(len(cols)):
            for j in range(len(self.columns)):
                if(cols[i] == self.columns[j]):
                    x.append(j)
                    break
                
        #x holds the indecies of the columns now
        data = relation()
        data.set_name("Result of " + str(cols) + " projection on " + self.name)
        data.set_columns(cols)
        #add rows
        for i in range(len(self.rows)):
            row = []
            for j in range(len(x)):
                row.append(self.rows[i][x[j]])
            data.add_row(row)
        return data
    
    @staticmethod
    def cartesian(relation_left, relation_right):
        #print("left relation = " + relation_left.get_name())
        #print("right relation = " + relation_right.get_name())
        #check that no shared column names
        left_cols = relation_left.get_column_names()
        right_cols = relation_right.get_column_names()
        tmp = []
        for i in range(len(left_cols)):
            tmp.append(left_cols[i])
        for i in range(len(right_cols)):
            if(right_cols[i] in left_cols):
                print("Invalid cartesian product query found - operation would result in non-unique columns")
                return None
            tmp.append(right_cols[i])
        #define dataset with columns
        data = relation()
        data.set_name("Result of cartesian product on " + relation_left.get_name() + " and " + relation_right.get_name())
        data.set_columns(tmp)
        left_rows = relation_left.get_rows()
        right_rows = relation_right.get_rows()
        #loop over left
        for i in range(len(left_rows)):
            #get lefthand row
            lefthand_side = []
            for j in range(len(left_rows[i])):
                lefthand_side.append(left_rows[i][j])
            #loop over righthand array
            for j in range(len(right_rows)):
                #tmp variable to store the final row
                tmp = []
                for k in range(len(lefthand_side)):
                    tmp.append(lefthand_side[k])
                #add right row elements to tmp
                for k in range(len(right_rows[j])):
                    tmp.append(right_rows[j][k])
                data.add_row(tmp)
        #for every row, add left row + right row as new row
        #return data
        return data

    @staticmethod
    def inner_join(relation_left, relation_right, arg):
        #perform cartesian on left and right
        result = relation.cartesian(relation_left, relation_right)
        #get the column names
        arg = arg[1:len(arg) - 1]
        arg = arg.split('=')
        col1 = arg[0]
        col2 = arg[1]
        #select based on query values
        result = result.column_join_operation(col1, col2)
        result.set_name("Result of inner join query on " + relation_left.get_name() + " and " + relation_right.get_name() + " with columns of " + col1 + ", " + col2)
        return result
    
    @staticmethod
    def outer_join(relation_left, relation_right, arg):
        #perform cartesian on left and right
        result = relation.cartesian(relation_left, relation_right)
        #get the column names
        arg = arg[1:len(arg) - 1]
        arg = arg.split('=')
        col1 = arg[0]
        col2 = arg[1]
        #select based on query values
        result = result.column_join_operation(col1, col2)
        result.set_name("Result of outer join query on " + relation_left.get_name() + " and " + relation_right.get_name() + " with columns of " + col1 + ", " + col2)
        #get the rows that are missing
        #for each row missing in left and right, add it with null data on the opposite side
        num_cols = len(result.get_column_names())
        num_cols_left = len(relation_left.get_column_names())
        num_cols_right = len(relation_right.get_column_names())
        rows = result.get_rows()
        #check what element is missing from first column of both left and right relation using get_column()
        #store indecies that are missing
        #loop over left and right relations and add rows to result based on indecies
        leftmost_column = relation_left.get_column(relation_left.get_column_names()[0])
        rightmost_column = relation_right.get_column(relation_right.get_column_names()[0])
        for i in range(len(rows)):
            #print("checking row " + str(rows[i]))
            for j in range(len(leftmost_column)):
                #print("against elements " + rows[i][0] + " and " + leftmost_column[j])
                if(rows[i][0] == leftmost_column[j]):
                    leftmost_column[j] = "NULL"
            for j in range(len(rightmost_column)):
                #print("against elements " + rows[i][num_cols_left] + " and " + rightmost_column[j])
                if(rows[i][num_cols_left] == rightmost_column[j]):
                    rightmost_column[j] = "NULL"
        #we now have empty columns in leftmost and rightmost column
        
        #loop over the columns in their respective tables, add num_cols_L/R 'NULL' to row then add data from relation
        #finally add row to result
        for i in range(len(leftmost_column)):
            if(leftmost_column[i] == "NULL"):
                continue
            tmp = relation_left.get_rows()
            row = []
            for j in range(len(tmp)):
                if(tmp[j][0] == leftmost_column[i]):
                    for k in range(len(tmp[j])):
                        row.append(tmp[j][k])
            for j in range(num_cols_right):
                row.append("NULL")
            result.add_row(row)
        #same algorithm but for right side, we add NULLs first because of data being flipped
        for i in range(len(rightmost_column)):
            if(rightmost_column[i] == "NULL"):
                continue
            tmp = relation_right.get_rows()
            row = []
            for j in range(num_cols_left):
                row.append("NULL")
            for j in range(len(tmp)):
                if(tmp[j][0] == rightmost_column[i]):
                    for k in range(len(tmp[j])):
                        row.append(tmp[j][k])
            result.add_row(row)
        return result
    
    @staticmethod
    def union(relation_left, relation_right):
        l_cols = relation_left.get_column_names()
        r_cols = relation_right.get_column_names()
        if(not l_cols == r_cols):
            print("Invalid union query found - not matching column names")
            return None
        #matching cols
        l_rows = relation_left.get_rows()
        r_rows = relation_right.get_rows()
        result = relation()
        result.set_columns(l_cols)
        #loop over left rows
        for i in range(len(l_rows)):
            #loop to check if left row exists in right dataset
            flag = False
            for j in range(len(r_rows)):
                #if it does move onto next left row
                if(l_rows[i] == r_rows[j]):
                    flag = True
                    break
                #otherwise add row to result
            if(not flag):
                result.add_row(l_rows[i])
        #we know that the rightside has unique rows only
        for i in range(len(r_rows)):
            result.add_row(r_rows[i])
        
        result.set_name("Result of union query on " + relation_left.get_name() + " and " + relation_right.get_name())
        return result
    
    @staticmethod
    def intersect(relation_left, relation_right):
        #intersection means it has to be present in both sets
        #we need to make sure we have identical columns for both sets
        #compare column names, get a list of identical columns
        l_cols = relation_left.get_column_names()
        r_cols = relation_right.get_column_names()
        cols = []
        for i in range(len(l_cols)):
            if(l_cols[i] in r_cols):
                cols.append(l_cols[i])
        for i in range(len(r_cols)):
            if(r_cols[i] in l_cols and not r_cols[i] in cols):
                cols.append(r_cols[i])
        #get the projection of that list of columns from both relations
        l_proj = relation_left.project(cols)
        r_proj = relation_right.project(cols)
        l_rows = l_proj.get_rows()
        r_rows = r_proj.get_rows()
        result = relation()
        result.set_columns(cols)
        result.set_name("Result of intersection query on " + relation_left.get_name() + " and " + relation_right.get_name())
        #loop over result of projection, compare (identically to union but checking for inequality)
        for i in range(len(l_rows)):
            #loop to check if left row exists in right dataset
            flag = True
            for j in range(len(r_rows)):
                #if it does move onto next left row
                if(l_rows[i] == r_rows[j]):
                    flag = False
                    break
                #otherwise add row to result
            if(not flag):
                result.add_row(l_rows[i])
        
        return result
    
    @staticmethod
    def subtract(relation_left, relation_right):
        l_cols = relation_left.get_column_names()
        r_cols = relation_right.get_column_names()
        if(not len(l_cols) == len(r_cols)):
            print("Invalid minus query found")
            return None
        result = relation()
        result.set_name("Result of minus query on " + relation_left.get_name() + " and " + relation_right.get_name())
        result.set_columns(l_cols)
        l_rows = relation_left.get_rows()
        r_rows = relation_right.get_rows()
        for i in range(len(l_rows)):
            if(not l_rows[i] in r_rows):
                result.add_row(l_rows[i])
        return result