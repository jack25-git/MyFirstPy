from lxml import etree

xml="""
<library>
    <book>
        <title>Python编程入门</title>
        <author>张三</author>
        <year>2023</year>
        <price>59.9</price>
    </book>
    <book>
        <title>数据结构与算法</title>
        <author>李四</author>
        <year>2024</year>
        <price>79.9</price>
    </book>
    <book>
        <title>机器学习实战</title>
        <author>王五</author>
        <year>2022</year>
        <price>89.9</price>
    </book>
</library>"""

tree=etree.XML(xml)

res=tree.xpath("/library/book/title/text()")
print(res)


