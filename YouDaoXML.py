from pathlib import Path
from tqdm import tqdm
import re
# from lxml import etree
# import xml.etree.ElementTree as ET
from dicttoxml import dicttoxml
from YouDaoWord import YouDaoWord


class YouDaoXML:
    def __init__(self, words=[]):
        self.words = words

    def add_word(self, word):
        """
        添加一个单词到单词列表中。
        """
        assert isinstance(word, YouDaoWord)
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
        if not words:
            words = self.words
        wordbook = {"wordbook": [i.as_dict() for i in words]}
        return dicttoxml(wordbook, root=False, attr_type=False).decode()

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
