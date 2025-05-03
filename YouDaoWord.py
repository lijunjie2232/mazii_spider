from pathlib import Path
from tqdm import tqdm
import re
import xml.etree.ElementTree as ET


class YouDaoWord:
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

    def __init__(self, word, trans="", phonetic="", tags="", progress=0):
        self.word = word
        self.trans = trans
        self.phonetic = phonetic
        self.tags = tags
        self.progress = progress

    def __str__(self):
        return f"<item>\n\t<word>{self.word}</word>\n\t<trans><![CDATA[{self.trans}]]></trans>\n\t<phonetic><![CDATA[{self.phonetic}]]></phonetic>\n\t<tags>{self.tags}</tags>\n\t<progress>{self.progress}</progress>\n</item>"

    def as_node(self):
        # 创建 <item> 元素
        item = ET.Element("item")

        # 创建并添加 <word> 元素
        word = ET.SubElement(item, "word")
        word.text = self.word

        # 创建并添加 <trans> 元素
        trans = ET.SubElement(item, "trans")
        trans.text = f"<![CDATA[{self.trans}]]>"

        # 创建并添加 <phonetic> 元素
        phonetic = ET.SubElement(item, "phonetic")
        phonetic.text = f"<![CDATA[{self.phonetic}]]>"

        # 创建并添加 <tags> 元素
        tags = ET.SubElement(item, "tags")
        tags.text = self.tags

        # 创建并添加 <progress> 元素
        progress = ET.SubElement(item, "progress")
        progress.text = self.progress

        return item
    
    def as_dict(self):
        """
            <item>
                <word>This is a Test这是单词 或者 句子</word>
                <trans><![CDATA[这是解释]]></trans>
                <phonetic><![CDATA[这是音标]]></phonetic>
                <tags>这是分类</tags>
                <progress>0</progress>
            </item>
        """
        return {
            "word": self.word,
            "trans": f"<![CDATA[{self.trans}]]>",
            "phonetic": f"<![CDATA[{self.phonetic}]]>",
            "tags": self.tags,
            "progress": self.progress,
        }

    def __repr__(self):
        return self.__str__()
