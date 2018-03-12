from unittest import TestCase, main

from crawler.utils import format_doc_number


class TestUtils(TestCase):
    def test_format_document_numner(self):
        doc_number = "09878976543451238976"

        formatted_doc_number = format_doc_number(doc_number)
        expected = "0987897-65.4345.1.23.8976"

        self.assertEqual(formatted_doc_number, expected)


if __name__ == "__main__":
    main()
