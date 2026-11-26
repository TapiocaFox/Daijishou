"""Validate the proposed localization with Python's standard library."""
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET

BASE = Path(__file__).resolve().parent
TOKEN = re.compile(r'%(?:\d+\$)?[-+# 0,(]*(?:\d+)?(?:\.\d+)?[a-zA-Z%]')

def validate():
    expected = json.loads((BASE / 'format-placeholders.json').read_text(encoding='utf-8'))
    root = ET.parse(BASE / 'values-zh-rCN/strings.xml').getroot()
    names = [node.attrib['name'] for node in root]
    assert len(names) == len(set(names)), 'Duplicate string resource'
    assert set(names) == set(expected), 'String inventory changed'
    for node in root:
        key = node.attrib['name']
        assert TOKEN.findall(node.text or '') == expected[key], f'Format tokens changed: {key}'
        assert node.tag == 'string' and node.text, f'Invalid string: {key}'
    arrays = ET.parse(BASE / 'values-zh-rCN/arrays.xml').getroot()
    lengths = {node.attrib['name']: len(node) for node in arrays}
    assert lengths == {'dark_mode_array': 3, 'home_page_id_display_name_array': 4, 'theme_color_display_array': 11}
    assert all(item.text for array in arrays for item in array)
    print(f'Valid: {len(root)} strings, {len(arrays)} arrays, {sum(lengths.values())} options; format tokens preserved.')

if __name__ == '__main__':
    validate()
