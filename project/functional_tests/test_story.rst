Let's do our setup::

    >>> from selenium.webdriver.firefox.webdriver import WebDriver
    >>> from selenium.webdriver.common.by import By
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

    >>> s.find_element(By.CSS_SELECTOR, ".practicearea a").click()
    >>> s.current_url.replace(url, '')
    '/practices/coaching/'

Go from there to the client page::

    >>> s.find_element(By.LINK_TEXT, "IBM").click()
    >>> s.current_url.replace(url, '')
    '/clients/ibm/'

This should talk about the consulting project::

    >>> "Coaching Project" in s.page_source
    True

Let's go to a consultant page::

    >>> s.find_element(By.PARTIAL_LINK_TEXT, "Who We Are").click()
    >>> s.find_element(By.LINK_TEXT, "Joel Burton").click()
    >>> s.current_url.replace(url, '')
    '/consultants/joel-burton/'

    >>> "<h1>Joel Burton</h1>" in s.page_source
    True

Clean up::

    >>> s.quit()

