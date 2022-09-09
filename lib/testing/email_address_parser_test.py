from email_address_parser import EmailAddressParser

class TestAnagram:
    '''Class Anagram in anagram.py'''

    def test_instantiates_with_string(self):
        '''instantiates with a single argument, a string.'''
        assert(EmailAddressParser("string string@string.com, mr. string, iamastring@icloud.com"))

    def test_has_parse_method(self):
        '''contains a method called "parse".'''
        assert(EmailAddressParser.parse)

    def test_parses_emails_with_spaces(self):
        '''finds emails with spaces in between.'''
        parser = EmailAddressParser("talk@talk.com john.jones@flatironschool.com alexa@amazon.com")
        assert(parser.parse() == ["alexa@amazon.com", "john.jones@flatironschool.com", "talk@talk.com"])

    def test_parses_emails_with_commas(self):
        '''finds emails with commas in between.'''
        parser = EmailAddressParser("talk@talk.com,john.jones@flatironschool.com,alexa@amazon.com")
        assert(parser.parse() == ["alexa@amazon.com", "john.jones@flatironschool.com", "talk@talk.com"])

    def test_parses_emails_with_commas_and_spaces(self):
        '''finds emails with commas and spaces in between.'''
        parser = EmailAddressParser("talk@talk.com, john.jones@flatironschool.com, alexa@amazon.com")
        assert(parser.parse() == ["alexa@amazon.com", "john.jones@flatironschool.com", "talk@talk.com"])

    def test_parses_emails_with_commas_and_spaces_and_non_emails(self):
        '''finds emails with commas and spaces in between and removes non-email strings.'''
        parser = EmailAddressParser("talk@talk.com, what john.jones@flatironschool.com, who alexa@amazon.com, where when why")
        assert(parser.parse() == ["alexa@amazon.com", "john.jones@flatironschool.com", "talk@talk.com"])