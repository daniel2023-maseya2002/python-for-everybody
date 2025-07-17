import xml.etree.ElementTree as ET

data = '''<person>
    <name>Daniel</name>
    <phone type ="intl">
        +250 791 434 027
    </phone>
    <email hide="yees"/>
</person>'''

tree = ET.fromstring(data)
print('Name:' ,tree.find('name').text)
print('Phone:', tree.find('phone').text.strip())
print('Attr:' ,tree.find('email').get('hide'))
