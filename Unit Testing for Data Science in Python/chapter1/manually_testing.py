# convert row to list
def row_to_list(row):
    row = row.rstrip()
    separated_entries = row.split("\\t")
    if len(separated_entries) == 2:
        return separated_entries
    return None


print(row_to_list("2,081\t314,942\n"))
print(row_to_list("\t293,410\n"))
print(row_to_list("1,463238,765\n"))


# # convert row to list after bugfix
def row_to_list_bugfix(row):
    row = row.rstrip()
    separated_entries = row.split("\\t")
    if len(separated_entries) == 2 and "" not in separated_entries:
        return separated_entries
    return None


print(row_to_list("2,081\t314,942\n"))
print(row_to_list("\t293,410\n"))
print(row_to_list("1,463238,765\n"))
