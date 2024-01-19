COMP 3005 - W24 - Challenge Assignment 1
Carleton University
Authour: Ben Granger
Student #101221725

HOW TO EXECUTE:
	To run the program, navigate to the directory with the 'source.py', 'relation.py', and 'queries.py' files in it.
	run the following command: 'python3 source.py' and follow the prompts.
	
HOW TO USE:
	When the program is run, the user will be prompted to enter a file with the relations and querie(s) that they wish
	to be executed. Once this filename is entered the result will be evaluated and displayed. Please refer to the 
	SYNTAX section to view the required syntax.

SYNTAX:
	In this section the required syntax for the submission file will be defined. All of the syntax is 'space sensitive',
	that is, blank spaces that are not EXPLICITY DEFINED in the following sections will cause syntax errors.
	
	RELATIONS:
		NAME (COLUMN_1, COLUMN_2, COLUMN_3, ...) = {
		ELEMENT_1, ELEMENT_2, ELEMENT_3, ...
		<ROW 2>
		<ROW 3>
		...
		}
		
		Notes: The elements within the relation's rows CAN NOT contain spaces (see 'KNOWN LIMITATIONS').
		<ROW 2>, <ROW 3>, ... follow the same syntax as the first row (containing ELEMENT_1, ELEMENT_2, ELEMENT_3, ...).
		The number of elements written on a single line does not have to align with the number of columns, the placement
		of the elements within the rows is determined by a modulo operator on the number of total elements.
	
	QUERIES:
		All Queries must follow the exact syntax (that is, if a column is specified on one side only a value cannot be 
		placed there, and vice versa). All query keywords are case sensitive. See KNOWN LIMITATIONS for more information.
		
		The RESULT of each Query can be NAMED. The syntax for that is as follows:
		
		NAME = QUERY
		
		SELECTION:
			select COLUMN<OPERATOR>VALUE(RELATION_NAME)
			
			Notes: As previously stated, there can be no spaces (especially in the second part after the select keyword)
			in this query. The column name must match a name in the specified relation. The supported operators are
			as follows: '=' - equals, '<' - less than, '>' - greater than.
		
		PROJECTION:
			proj COLUMN_1 COLUMN_2 COLUMN_3 ... (RELATION_NAME)
			
			Notes: Each of the specified columns must exist in the given relation. No duplicate columns are allowed.
			The column names are case-sensitive.
		
		CARTESIAN PRODUCT:
			RELATION_A_NAME cartesian RELATION_B_NAME
			
			Notes: This operation is commutative. That is, the same result will be returned with the operands flipped.
			The two relations CAN NOT have any columns with identical names (case sensitive).
		
		INNER JOIN:
			RELATION_A_NAME innerjoin (COLUMN_1=COLUMN_2) RELATION_B_NAME
			
			Notes: This operation is commutative. That is, the same result will be returned with the operands flipped.
			The two relations CAN NOT have any columns with identical names (case sensitive). There must be one column
			from each relation specified.
			
		OUTER JOIN (FULL OUTER JOIN):
			RELATION_A_NAME outerjoin (COLUMN_1=COLUMN_2) RELATION_B_NAME
			
			Notes: This operation is commutative. That is, the same result will be returned with the operands flipped.
			The two relations CAN NOT have any columns with identical names (case sensitive). There must be one column
			from each relation specified.
		
		UNION:
			RELATION_A_NAME union RELATION_B_NAME
			
			Notes: This operation is commutative. That is, the same result will be returned with the operands flipped.
			ALL columns from both operations must be identical (case sensitive), and there must be the same number
			of columns in both relations.
		
		INTERSECTION:	
			RELATION_A_NAME intersect RELATION_B_NAME
			
			Notes: ALL columns from both operations must be identical (case sensitive), and there must be the same number
			of columns in both relations.
			
		SUBTRACTION:
			RELATION_A_NAME minus RELATION_B_NAME
			
			Notes: There must be an identical number of columns in both relations.
		
KNOWN LIMITATIONS (for marking purposes):
	All operations are extremely case and space sensitive in this program. This is by far the largest limitation as it
	causes the syntax to be very constrictive. The selection query does not include the '<=', '>=' or '!=' operators 
	as I could not figure out a way to implement it. I have implemented inner and outer join operations but have left
	out the sister operations of outer join due to time restraints and it not being specified in the specifications.
	I have not included the division operator as it is not a set operation and was not specified in the specifications.
	
	If there are any questions feel free to contact myself at: bengranger3@cmail.carleton.ca
	
	Thank you.