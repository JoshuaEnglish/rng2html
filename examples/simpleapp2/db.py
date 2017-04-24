import os
from lxml import etree

input_dir = os.path.join(os.path.split(__file__)[0], 'data')

if not os.path.exists(input_dir):
    raise ValueError("Cannot find input path %s" % input_dir)

ADDRESSES = []

def get_addresses():
    """Return a list of dictionaries"""
    doc = etree.parse(os.path.join(input_dir, "addressbook.xml"))
    res = []
    for card in doc.iter('card'):
        res.append({'name': card.findtext('name'),
                   'email': card.findtext('email')})
    return res
    