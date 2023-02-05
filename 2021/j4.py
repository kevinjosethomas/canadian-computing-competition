# Arranging Books - 15/15

bookshelf = input()

sorted_bookshelf = bookshelf.count("L") * "L" + bookshelf.count("M") * "M" + bookshelf.count("S") * "S"

l_end = bookshelf.count("L")
m_end = l_end + bookshelf.count("M")

l_range, m_range, s_range = bookshelf[:l_end], bookshelf[l_end:m_end], bookshelf[m_end:]

print(l_range.count("M") + l_range.count("S") + max(m_range.count("S"), s_range.count("M")))
