import allure
import pytest


@allure.title("Test check policy page header and url")
@allure.description("Open policy page and check its url and header text.")
@allure.tag("Url", "Header", "Policy", "Text")
@allure.label("owner", "Mary Gold")
@pytest.mark.smoke
def test_policy_page_url(open_policy_page):
    policy_page = open_policy_page
    assert policy_page.get_biggest_header_text() == "Privacy Policy", "Incorrect privacy policy h1"
    assert policy_page.get_page_url() == "https://refactoring.guru/uk/privacy-policy", \
        "Incorrect privacy policy page url"


@allure.title("Test check 'go to google policy link' is functional")
@allure.description("Open policy page and go to the google policies page via link."
                    " Check its url and first paragraph text. ")
@allure.tag("Url", "Paragraph", "Policy", "Text", "Link")
@allure.label("owner", "Mary Gold")
@pytest.mark.regression
def test_go_to_google_policies_link(open_policy_page):
    policy_page = open_policy_page
    policy_page.click_google_policies_link()
    assert policy_page.get_google_policies_first_paragraph_text() == ("When you use our services, you’re trusting us"
                                                                      " with your information. We understand this is a"
                                                                      " big responsibility and work hard to protect"
                                                                      " your information and put you in control."), \
        "Incorrect google policy warning"
    assert policy_page.get_page_url() == "https://policies.google.com/privacy?hl=en", "Incorrect google policy page url"


@allure.title("Test warning text about using personal data")
@allure.description("Open policy page and check there is text about using personal data.")
@allure.tag("Policy", "Text", "Personal data", "Warning")
@allure.label("owner", "Mary Gold")
@pytest.mark.smoke
def test_warning_about_using_personal_data(open_policy_page):
    policy_page = open_policy_page
    warning_text = ("We use your data to provide and improve the Service."
                    " By using the Service, you agree to the collection and use of information"
                    " in accordance with this policy. Unless otherwise defined in this Privacy Policy,"
                    " terms used in this Privacy Policy have the same meanings as in our Terms and Conditions,"
                    " accessible from https://refactoring.guru")
    assert warning_text in policy_page._page.get_page_source(), \
        "The warning about using personal data is incomplete or missing"


@allure.title("Test personal data list info")
@allure.description("Open policy page and check the number of clauses about personal data and its text.")
@allure.tag("Policy", "Text", "Personal data", "List", "Count")
@allure.label("owner", "Mary Gold")
@pytest.mark.regression
def test_personal_data_list(open_policy_page):
    policy_page = open_policy_page
    exp_count = 5
    assert policy_page.get_count_personal_data() == exp_count, f"There should be {exp_count} items"
    assert policy_page.get_personal_data_li_text(index=1)["info"] == "Email address", "Should see: Email address"
    assert policy_page.get_personal_data_li_text(index=2)["info"] == "First name and last name", \
        "Should see: First name and last name"
    assert policy_page.get_personal_data_li_text(index=3)["info"] == "Phone number", "Should see: Phone number"
    assert policy_page.get_personal_data_li_text(index=4)["info"] == "Address, State, Province, ZIP/Postal code, City", \
        "Should see: Address, State, Province, ZIP/Postal code, City"
    assert policy_page.get_personal_data_li_text(index=5)["info"] == "Cookies and Usage Data", \
        "Should see: Cookies and Usage"


@allure.title("Test advert policy page")
@allure.description("Open policy page and go to advert policy page via link. Check its url and introduction text.")
@allure.tag("Policy", "Text", "Advert", "Url")
@allure.label("owner", "Mary Gold")
@pytest.mark.regression
def test_advert_policy(open_policy_page):
    policy_page = open_policy_page
    policy_page.click_advert_policy_link()
    introduction = ("Most online ads are not targeted to you as an individual but rather to data"
                    " categories such as your probable demographics (age, gender), interests "
                    "(automobiles, travel, shoes), location, websites visited and apps used.")
    assert introduction in policy_page._page.get_page_source(), \
        "The introduction about advertising is incomplete or missing"
    assert policy_page.get_page_url() == "https://youradchoices.ca/", "Incorrect advertising policy url"


@allure.title("Test usage policy page")
@allure.description("Open policy page and go to usage policy page via link. Check its url."
                    " Also check text about citations and illustrations.")
@allure.tag("Policy", "Text", "Url", "Usage")
@allure.label("owner", "Mary Gold")
@pytest.mark.regression
def test_usage_policy(open_policy_page):
    policy_page = open_policy_page
    policy_page.click_usage_content_link()
    citation_text = ("Ви можете цитувати будь-який текст на цьому сайті,"
                     " якщо ваша цитата не є суттєвою частиною цитованої статті.")
    illustration_text = ("Ви можете використовувати до 10 ілюстрацій з цього сайту для всіх"
                         " ваших публікацій та презентацій.")
    assert policy_page.get_citation_info_text() == citation_text, "Incorrect citation usage info"
    assert policy_page.get_illustration_info_text() == illustration_text, "Incorrect illustration usage info"
    assert policy_page.get_page_url() == "https://refactoring.guru/uk/content-usage-policy", \
        "Incorrect usage policy url"
