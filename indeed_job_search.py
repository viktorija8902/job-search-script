from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# http://selenium-python.readthedocs.io/locating-elements.html#locating-by-xpath
browser = webdriver.Chrome()
browser.get('https://www.indeed.ca/')

advanced_search_link = browser.find_element_by_link_text('Advanced Job Search')
advanced_search_link.click()

filter_out_postings_with_words = browser.find_element_by_id('as_not')
filter_out_postings_with_words.send_keys('stress stressful multitasking multitask pressure wordpress drupal')

words_in_title = browser.find_element_by_id('as_ttl')
words_in_title.send_keys('software developer')

# exact location only
location_radius = browser.find_element_by_xpath("//select[@id='radius']/option[@value=0]")
location_radius.click()

# age of postings: 7 days
posting_age = browser.find_element_by_xpath("//select[@id='fromage']/option[@value=7]")
posting_age.click()

# show 50 job postings per page
results_per_page = browser.find_element_by_xpath("//select[@id='limit']/option[@value=50]")
results_per_page.click()

sort_by_date = browser.find_element_by_xpath("//select[@id='sort']/option[@value='date']")
sort_by_date.click()

submit_button = browser.find_element_by_id('fj')
submit_button.click()
