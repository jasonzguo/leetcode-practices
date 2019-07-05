"""
    Problem:
        Longest Common Subsequence

    Lessons Learned:
        - should think outside of the box
        - learning from other people's code, and experience
"""

import sure


def solution(strA, strB):
    strA_length = len(strA)
    strB_length = len(strB)

    # strA will be represented by columns
    # strB will be represented by rows
    table = [[0 for x in range(strA_length + 1)]
             for y in range(strB_length + 1)]

    for rowIndex, row in enumerate(table[1:]):
        for columnIndex, column in enumerate(row[1:]):
            if strB[rowIndex] == strA[columnIndex]:
                table[rowIndex + 1][columnIndex +
                                    1] = table[rowIndex][columnIndex] + 1
            else:
                table[rowIndex + 1][columnIndex + 1] = max(
                    table[rowIndex + 1][columnIndex],
                    table[rowIndex][columnIndex + 1])

    current_row_index = strB_length
    current_column_index = strA_length
    current_table_value = table[current_row_index][current_column_index]
    result = ''
    while current_table_value > 0:
        if table[current_row_index][current_column_index -
                                    1] == current_table_value:
            current_column_index -= 1
        elif table[current_row_index -
                   1][current_column_index] == current_table_value:
            current_row_index -= 1
        else:
            current_row_index -= 1
            current_column_index -= 1
            current_table_value = table[current_row_index][
                current_column_index]
            result = strB[current_row_index] + result
    return result


solution('ABCDGH', 'AEDFHR').should.equal('ADH')
solution('AGGTAB', 'GXTXAYB').should.equal('GTAB')
solution('aaaa', 'aa').should.equal('aa')
solution('ccc', 'aa').should.equal('')
solution('aa', 'aa').should.equal('aa')
print('ok')
