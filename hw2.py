import itertools
import os
import re
import sys
from pathlib import Path
from typing import Optional, Union

import nltk
from bs4 import BeautifulSoup
from nltk.corpus import CorpusReader
from nltk.probability import FreqDist


""" Problem 1: Python Exercises """


def function_without_implementation():
    raise NotImplementedError("This function has no implementation.")


""" Problem 2: Analysis of Inaugural Addresses """


def get_encodings(corpus: CorpusReader) -> dict[str, str]:
    """
    Problem 2c: Identifies the encoding for each file in an NLTK corpus.
    This function assumes that the encoding of a file is utf8 if it
    contains at least one token ending in "â" when loaded in latin1 en-
    coding. Otherwise, this function assumes that the file's encoding is
    latin1.

    :param corpus: An NLTK corpus
    :return: A dict mapping each file in corpus.fileids() to its en-
        coding (either "utf8" or "latin1")
    """
    old_encoding = corpus._encoding
    corpus._encoding = "latin1"
    encodings = dict()
    for file in corpus.fileids():
        encodings[file] = "latin1"
        for w in corpus.words(file):
            if w.endswith("â"):
                encodings[file] = "utf8"
                break
    corpus._encoding = old_encoding
    return encodings


""" Problem 3: Analysis of Nomination Acceptance Speeches """

# Download the default NLTK tokenizer if it's not installed already
nltk.download("punkt_tab")


def get_raw_text_from_html(filename: str) -> str:
    """
    Problem 3a: Extracts the text of an HTML file containing a nomina-
    tion acceptance speech from the American Presidency Project website.
    Paragraphs of the text (represented by p elements in the HTML code)
    should be separated by '\n'.

    :param filename: The name of an HTML file containing a speech
    :return: The text of the speech
    """
    with open(filename, "r") as f:
        soup = BeautifulSoup(f, features="html.parser")
    speech = soup.find_all("div", {"class": "field-docs-content"})
    return "\n".join(p.get_text() for p in speech[0].children)


def preprocess(raw_text: str) -> str:
    """
    Removes substrings of the form "[...]" from a string.

    :param raw_text: A string
    :return: raw_text, with anything between square brackets removed
    """
    return re.sub(r"\[.*]", "", raw_text)


class ConventionSpeechCorpus:
    """
    A container for nomination acceptance speeches represented as HTML
    files. This class is a simplified version of the NLTK CorpusReader.
    """

    def __init__(self, filename_or_folder: Optional[str] = None):
        """
        When a ConventionSpeechCorpus object is constructed, this method
        initializes it by loading one or more HTML files into it. More
        HTML files can be added to the ConventionSpeechCorpus using the
        .add method.

        :param filename_or_folder: An HTML file to be loaded into the
            corpus or a folder containing HTML files, all of which will
            be loaded into the corpus
        """
        self._raw_texts = dict()
        if filename_or_folder.endswith(".html"):
            self.add(filename_or_folder)
        elif filename_or_folder is not None:
            """
            Problem 3c: In this branch of the if-else block, you can
            assume that filename_or_folder is the name of a folder. 
            Please add all HTML files in this folder to self._raw_texts.
            """
            folder = filename_or_folder
            for filename in sorted(os.listdir(folder)):
                if filename.endswith(".html"):
                    self.add(f"{filename_or_folder}/{filename}")

    def add(self, filename: str):
        raw = preprocess(get_raw_text_from_html(filename))
        self._raw_texts[filename] = raw

    """ NLTK Corpus Methods """

    def fileids(self) -> list[str]:
        return list(self._raw_texts.keys())

    def raw(self, files: Union[str, list[str], None] = None) -> str:
        """
        Problem 3d: Returns the raw text from self._raw_texts for one or
        more files in the corpus, depending on the value of the files
        parameter.
        - If files is the name of a file, then the raw text for that
          file is returned.
        - If files is a list of files, then the raw text for those files
          is returned, in the same order that the files appear in files.
        - If files is None, then the raw text for all files is returned,
          in lexicographic order of their filenames (Python's default
          sort order for the filenames).
        - If files contains at least one file not represented in
          self._raw_texts, this method should raise a ValueError.
        If raw texts are returned for more than one file, they should be
        separated by '\n'.

        :param files: The name of a file, or a list of files
        :return: The raw text for the files(s) described by files. If
            files is None, then the raw text for all files is returned
        """
        if files is None:
            return "\n".join(self._raw_texts.values())
        elif isinstance(files, list):
            return "\n".join(self.raw(fn) for fn in files)
        elif files in self._raw_texts:
            return self._raw_texts[files]
        else:
            raise ValueError(f"There is no file called {files} "
                             "in this corpus!")

    def words(self, files: Union[str, list[str], None] = None) -> list[str]:
        """
        Problem 3d: Returns text for one or more files in the corpus,
        preprocessed using the preprocess function and tokenized using
        the nltk.word_tokenize function. Which files are included in the
        tokenized text depends on the value of the files parameter.
        - If files is the name of a file, then the tokens for the text
          from that file is returned.
        - If files is a list of files, then the tokens for the text in
          those files is returned, in the same order that the files
          appear in files.
        - If files is None, then the tokens for the text in all files is
          returned, in lexicographic order of their filenames (Python's
          default sort order for the filenames).
        - If files contains at least one file not represented in
          self._raw_texts, this method should raise a ValueError.
        If lists of tokens are returned for more than one file, they
        should be concatenated.
        
        :param files: The name of a file, or a list of files
        :return: The tokenized text from the files(s) described by
            files. If files is None, then the tokenized text for all
            files is returned
        """
        raw_text = self.raw(files)
        return nltk.word_tokenize(raw_text)
