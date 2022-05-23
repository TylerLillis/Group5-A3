'''
Uses Python to parse module data from the data.xml file.
I created an data.xml as an example file to parse data from.
Note: Use loops to find the modules, DO NOT HARDCODE THE AMOUNT IT'S LOOKING FOR

--Teaching Section--
What needs to be parsed:
- Module name
- No. of sections
- Completed sections

And for each individual section:
- Page number
- Page layout type
- Body of the page

--Testing Section--
What needs to be parsed:
- Questions and answers from completed modules
'''

#Import required modules
import xml.etree.ElementTree as et
import os
import sys

tree = et.parse(os.path.join(sys.path[0], "Data.xml"))
root = tree.getroot()

#Parse required data for teaching section
for module in root:
    print('Module name:', module.attrib['name'])
    print('Number of sections:', module[0].text)
    print('Completed?:', module[1].text)

    SectionNum = 1
    for section in module[2]:
        print('   Section', SectionNum)
        SectionNum += 1
        for page in section[0]:
            print('Page number:',page.attrib['num'])
            print('Page layout:', page[0].text)
            print('Page body:', page[1].text)
    print('\n')
    
#Parse required data for testing section
for module in root:
    if module[1].text == 'Yes':
        for question in module[3]:
            print('Question:', question[0].text)
            print('Answer:', question[1].text)