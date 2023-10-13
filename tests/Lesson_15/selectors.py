# Find the web page.
#
# Write 30 XPATH locators for this page using XPath. Some of them should have more than 3 steps.
#
# For 10 XPATH locators write 10 CSS locators which find the same element

# https://refactoring.guru/uk

# xpath

loc_signature_paragraph = "//div[@class='author row']/p[last()]"
# спираємось на class елемента div

loc_p_s_paragraph = "//p[@class='col-12 col-sm-6 col-md-8']"
# спираємось на class елемента p

loc_lang_btn = "//ul[@class='navigation-menu']/li[1]/button[1]"

loc_autumn_sale_btn = "//span[@class='announcement-link-text']"

loc_top_wine_img = "//div[starts-with(@class,'announcement')]/a/img[3]"

loc_top_coon_logo_img = "//aside[@class='sidebar main-menu']/following-sibling::nav/div/a/img"  # верхня картинка єнота
# уявимо, що маємо тільки клас елементу aside

loc_top_boy_with_book_img = "//div[starts-with(@class, 'announ')]/a/img[1]"

loc_top_cup_tea_img = "//div[starts-with(@class, 'announ')]/a/img[2]"

loc_top_tree_leaf_img = "//span[starts-with(@class, 'announ')]/following-sibling::img[2]"

loc_top_nav_cont = "//div[@class='navigation-container']"

loc_biggest_header = "//div[starts-with(@class, 'main-content')]/div[2]/h1"  # or just "//h1"

loc_email_input = "//*[@type='email' and @id='email']"

loc_email_news_header = "//*[@class='email banner']/h3"

loc_email_paragraph = "//*[@class='email banner']/p"

loc_facebook_banner = "//*[@class='facebook banner']"

loc_facebook_banner_header = "//div[@class='facebook banner']/h3"

loc_facebook_banner_img = "//div[@class='facebook banner']/p/a/img"

loc_coon_with_cars_img = "//h2[text()='Рефакторинг']/../../div[@class='col-md-6' and @aria-hidden='true']/a/img"
# варіант з "підійманням", якщо б було потрібно почати з хедера

loc_coon_with_cars_v2_img = "//div[@class='col-md-6' and @aria-hidden='true']/a/img"
# варіант без "підіймання"

loc_refactoring_header = "//h2[text()='Рефакторинг']"

loc_refactoring_paragraph = "//h2[text()='Рефакторинг']/following-sibling::p"

loc_go_to_refactoring_btn = "//h2[text()='Рефакторинг']/following-sibling::a"

loc_pattern_types_img = "//div[@class='container-fluid container-headline'][2]/div/div[1]/a/img"

loc_patterns_header = "//div[@class='col-md-6' and @aria-hidden='true']/h2"

loc_patterns_paragraph = "//div[@class='col-md-6' and @aria-hidden='true']/p"

loc_go_to_patterns_btn = "//div[@class='col-md-6' and @aria-hidden='true']/p/following-sibling::a"

loc_footer_container = "//footer[@class='footer center-content']/div[1]/div[1]"

loc_footer_list = "//div[@class='col-8 col-sm-12']/ul"

loc_footer_spanish_office_text = "//*[text()='Spanish office:']"

loc_footer_about_us_text = "//*[text()='About us']"

loc_footer_copyright_symbol = "//*[@class='fa fa-fw fa-copyright']"

# css

loc_paragraph_signature_css = "p.col-12.col-sm-6.col-md-4.signature"
# спираємось на class елемента p

loc_paragraph_p_s_css = "div.author.row > :first-child"
# спираємось на class елемента div

loc_top_wine_img_css = "span[class*='announ'] + img"

loc_top_tree_leaf_img_css = "span[class*='announ'] + img + img"

loc_top_coon_logo_img_css = "a.navigation-brand > :last-child"

loc_biggest_header_css = "div.page.text h1"

loc_email_input_css = "input#email"

loc_facebook_banner_css = "div.facebook.banner"

loc_footer_list_css = "div.col-8.col-sm-12 ul.footer-list"

loc_footer_copyright_symbol_css = "div.col-12.col-sm-8 > :first-child"




