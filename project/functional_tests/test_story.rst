Let's do our setup::

    >>> from selenium.webdriver.firefox.webdriver import WebDriver
    >>> s = WebDriver()

    >>> from consulting.tests import factories
    >>> coaching = factories.PracticeAreaFactory(status='published')
    >>> ibm = factories.ClientFactory(status='published')
    >>> ibm.practiceareas.add(coaching)
    >>> coaching_work = factories.ClientWorkFactory(status='published')
    >>> joel = factories.ConsultantFactory(status='published')

Start at the homepage::

    >>> s.get(url)

Follow the link to coaching::

    >>> s.find_element_by_css_selector(".practicearea a").click()
    >>> s.current_url.replace(url, '')
    u'/practices/coaching/'

Go from there to the client page::

    >>> s.find_element_by_link_text("IBM").click()
    >>> s.current_url.replace(url, '')
    u'/clients/ibm/'

This should talk about the consulting project::

    >>> "Coaching Project" in s.page_source
    True

Let's go to a consultant page::

    >>> s.find_element_by_partial_link_text("Who We Are").click()
    >>> s.find_element_by_link_text("Joel Burton").click()
    >>> s.current_url.replace(url, '')
    u'/consultants/joel-burton/'

    >>> "<h1>Joel Burton</h1>" in s.page_source
    True

Clean up::

    >>> s.quit()

