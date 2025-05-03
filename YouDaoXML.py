from pathlib import Path
from tqdm import tqdm
import re
import xml.etree.ElementTree as ET


class YouDaoXML:
    def __init__(self, words=[]):
        self.words = words

    def add_word(self, word):
        """
        添加一个单词到单词列表中。
        """
        self.words.append(word)

    def as_xml(self, words=None):
        """
        返回包含所有单词的完整 XML 文档。
        """
        """
        <wordbook>
            <item>
                <word>This is a Test这是单词 或者 句子</word>
                <trans><![CDATA[这是解释]]></trans>
                <phonetic><![CDATA[这是音标]]></phonetic>
                <tags>这是分类</tags>
                <progress>0</progress>
            </item>
        </wordbook>
        """
        # 创建 <wordbook> 根元素
        wordbook = ET.Element("wordbook")

        # 遍历所有单词，将每个单词转换为 XML 节点并添加到 <wordbook> 中
        if words:
            for word in words:
                wordbook.append(word.as_node())
        else:
            for word in self.words:
                wordbook.append(word.as_node())

        # 将 ElementTree 对象转换为字符串
        xml_str = ET.tostring(wordbook, encoding="unicode", method="xml")
        del wordbook
        return xml_str

    def save_xml(self, file_path, words=None):
        """
        将 XML 文档保存到指定路径的文件中。
        """
        # 将 XML 文档转换为字符串
        xml_str = self.as_xml(words).replace("&gt;", ">").replace("&lt;", "<")

        # 将字符串写入文件
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(xml_str)

        return file_path
