from tuple_assign import assign_integer, assign_list
    
tuple_integer = (0,)
print("tuple_integer before += :", tuple_integer)
assign_integer(tuple_integer)
print("tuple_integer after += :", tuple_integer)

print()

tuple_list : tuple[list[str]] = ([],)
print("tuple_list before += :", tuple_list)
assign_list(tuple_list)
print("tuple_list after += :", tuple_list)
