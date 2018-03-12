def format_doc_number(doc_number):
    place_holder = "{0}-{1}.{2}.{3}.{4}.{5}"

    first_chunk = slice(0, 7)
    second_chunk = slice(7, 9)
    third_chunk = slice(9, 13)
    fourth_chunk = slice(13, 14)
    fifth_chunk = slice(14, 16)
    sixth_chunk = slice(16, 20)

    return place_holder.format(
        doc_number[first_chunk],
        doc_number[second_chunk],
        doc_number[third_chunk],
        doc_number[fourth_chunk],
        doc_number[fifth_chunk],
        doc_number[sixth_chunk]
    )
