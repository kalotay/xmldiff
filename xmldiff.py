def flatxmldiff(left, right):
    left_diff = []
    right_diff = []
    left_iter = left.__iter__()
    right_iter = right.__iter__()
    try:
        left_value = left_iter.__next__()
        right_value = right_iter.__next__()
        while True:
            if left_value > right_value:
                right_diff.append(right_value)
                right_value = right_iter.__next__()
            elif left_value < right_value:
                left_diff.append(left_value)
                left_value = left_iter.__next__()
            else:
                right_value = right_iter.__next__()
                left_value = left_iter.__next__()
    except StopIteration:
        pass
    return (left_diff, right_diff)

def flattenxmlrec(xml, buffer, keys):
    key = xmlsortkey(xml)
    keys.append(key)
    if xml.text:               
        final_key = tuple(keys)
        buffer.append((final_key, xml.text))
    for x in sorted(xml,key=xmlsortkey):
        flattenxmlrec(x, buffer, keys)
    keys.pop()

def flattenxml(xml):                 
    flat_xml = []
    keys = []
    flattenxmlrec(xml, flat_xml, keys)
    return flat_xml

