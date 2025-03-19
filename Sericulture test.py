from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import unittest
import pandas as pd
import logging

class TestRequiredInputFieldWithLogin(unittest.TestCase):

    def setUp(self):
        # Initialize the WebDriver with desired user agent
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://bda.bsdbpims.com/login')  

    def test_required_input_field(self):
        driver = self.driver
        
        # Print the title of the page
        print("Initial page title: ", driver.title)    

        # Login process
        try:
            username_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'email'))  
            )
            password_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'password')) 
            )
            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[text()="Sign in"]'))  
            )
        except TimeoutException:
            print("Login elements not found on the page")
            return

        username_field.send_keys('akmal@bsdbpims.com')  
        password_field.send_keys('1234567#8')  
        login_button.click()

        # Print current state
        print("Login button clicked")

        # Check for an element that confirms successful login
        try:
            dashboard_element = WebDriverWait(driver, 25).until(
                EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Dashboard')]"))  # replace with an element that confirms login
            )
            print("Login successful, Dashboard found")
        except TimeoutException:
            print("Login failed or redirected to an unexpected page.")
            print(f"Current URL after login attempt: {driver.current_url}")
            return



      # Wait until the "Members" link is present and clickable

        try:
         members_link = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "//a[@href='https://bda.bsdbpims.com/admin/users' and contains(@class, 'nav-link')]"))
         )
    
         # Step 2: Click the "Members" link
         members_link.click()
         print("Members link clicked successfully")

        except TimeoutException:
         print("Members link not found or not clickable")


        #User form fill process
        
        # Configure logging
        logging.basicConfig(filename='form_submission.log', level=logging.INFO) 

        # Read data from Excel file
        df = pd.read_excel('User_Sericulture.xlsx', dtype={'Mobile No.': str})
        time.sleep(10)
      # Iterate over each user
        for index, row in df.iterrows(): 
             try:
                 # Wait until the button becomes visible and clickable
                 button = WebDriverWait(driver, 10).until(
                  EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'btn-primary')]"))
                  )
                 # Check if the button is displayed on the page
                 if button.is_displayed() and button.is_enabled():
                     print("Button is visible and clickable. Now clicking...")
                     button.click()  # Perform the click action
                 else:
                     print("Button is not clickable.")

                 name_field = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.ID, 'InputName')) )
                 name_field.clear()
                 name_field.send_keys(row['Name'])

                 fname_field = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[1]/div[2]/input')) )
                 fname_field.clear()
                 fname_field.send_keys(row['fathers name'])

                 mname_field = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[1]/div[3]/input')) )
                 mname_field.clear()
                 mname_field.send_keys(row['mothers name'])

                 sname_field = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[1]/div[4]/input')) )
                 sname_field.clear()
                 sname_field.send_keys(row['spouse name'])

                 nid_no_field = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.ID, 'NIDBCN')))
                 nid_no_field.clear()
                 nid_no_field.send_keys(row['NID no.'])

                 Mobile_no_field = WebDriverWait(driver, 10).until(
                 EC.element_to_be_clickable((By.ID, 'InputTel')))
                 Mobile_no_field.clear()
                 Mobile_no_field.send_keys(row['Mobile No.'])

                 village = WebDriverWait(driver, 10).until(
                 EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[3]/div[3]/input')))
                 village.clear()
                 village.send_keys(row['village'])

                 email = WebDriverWait(driver, 10).until(
                 EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[2]/div[3]/input')))
                 email.clear()
                 email.send_keys(row['email'])

                 #for gender feild
                 dropdown_element = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[3]/div[1]/select'))
                 )
                 gender = str(row['gender'])
                 # Create a Select object for interacting with the dropdown
                 select = Select(dropdown_element)
                 # Select the option by visible text
                 select.select_by_visible_text(gender) 

                 #for religion feild
                 dropdown_element = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[3]/div[2]/select'))
                 )
                 religion = str(row['religion'])
                 # Create a Select object for interacting with the dropdown
                 select = Select(dropdown_element)
                 # Select the option by visible text
                 select.select_by_visible_text(religion)

                 #for division feild
                 dropdown_element = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[4]/div[1]/select'))
                 )
                 division = str(row['division'])
                 # Create a Select object for interacting with the dropdown
                 select = Select(dropdown_element)
                 # Select the option by visible text
                 select.select_by_visible_text(division)


                 #for district feild
                 dropdown_element = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[4]/div[2]/select'))
                 )
                 district = str(row['district'])
                 # Create a Select object for interacting with the dropdown
                 select = Select(dropdown_element)
                 # Select the option by visible text
                 select.select_by_visible_text(district)

                 #for thana feild
                 dropdown_element = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[4]/div[3]/select'))
                 )
                 thana = str(row['thana'])
                 # Create a Select object for interacting with the dropdown
                 select = Select(dropdown_element)
                 # Select the option by visible text
                 select.select_by_visible_text(thana)

                 #for project feild
                 dropdown_element = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[5]/div[1]/select'))
                 )
                 project = str(row['project'])
                 # Create a Select object for interacting with the dropdown
                 select = Select(dropdown_element)
                 # Select the option by visible text
                 select.select_by_visible_text(project)

                 #for project type feild
                 dropdown_element = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[5]/div[2]/select'))
                 )
                 project_type = str(row['project type'])
                 # Create a Select object for interacting with the dropdown
                 select = Select(dropdown_element)
                 # Select the option by visible text
                 select.select_by_visible_text(project_type)

                 #for project sub type feild
                 dropdown_element = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[5]/div[3]/select'))
                 )
                 project_sub_type = str(row['project sub-type'])
                 # Create a Select object for interacting with the dropdown
                 select = Select(dropdown_element)
                 # Select the option by visible text
                 select.select_by_visible_text(project_sub_type)

                 #for geo_location feild
                 dropdown_element = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[6]/div[1]/select'))
                 )
                 geo_location = str(row['geo-location'])
                 # Create a Select object for interacting with the dropdown
                 select = Select(dropdown_element)
                 # Select the option by visible text
                 select.select_by_visible_text(geo_location)


                 #for office feild
                 dropdown_element = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[6]/div[2]/select'))
                 )
                 office = str(row['office'])
                 # Create a Select object for interacting with the dropdown
                 select = Select(dropdown_element)
                 # Select the option by visible text
                 select.select_by_visible_text(office)

                 #for center feild
                 dropdown_element = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[6]/div[3]/select'))
                 )
                 center = str(row['center'])
                 # Create a Select object for interacting with the dropdown
                 select = Select(dropdown_element)
                 # Select the option by visible text
                 select.select_by_visible_text(center)


                 harvest_money = WebDriverWait(driver, 10).until(
                 EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[7]/div/div[1]/div/input')))
                 harvest_money.clear()
                 harvest_money.send_keys(row['harvest money'])

                 poolghor = WebDriverWait(driver, 10).until(
                 EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[7]/div/div[2]/input')))
                 poolghor.clear()
                 poolghor.send_keys(row['poolghor'])

                 mulberry_cult = WebDriverWait(driver, 10).until(
                 EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[8]/div/div[1]/input')))
                 mulberry_cult.clear()
                 mulberry_cult.send_keys(row['mulberry_cult'])


                 duration_cult = WebDriverWait(driver, 10).until(
                 EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[9]/div[2]/input')))
                 duration_cult.clear()
                 duration_cult.send_keys(row['duration_cult'])
                 

                 #for project year feild
                 dropdown_element = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((By.XPATH, '//html//body//div[2]//div[1]//div//div//span//div[1]//div//div[9]//div[1]//select'))
                 )
                 project_year = str(row['Year'])
                 # Create a Select object for interacting with the dropdown
                 select = Select(dropdown_element)

                 # Select the option by visible text
                 select.select_by_visible_text(project_year) 

                 print(f"Selected option: {project_year}")


                 # Log success
                 logging.info(f"Successfully submitted form for {row['Name']} {row['NID no.']}")

                 Submit_button = WebDriverWait(driver, 10).until(
                 EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div/div/span/div[1]/div/div[11]/div/button[1]")))
                 Submit_button.click()  

                 print("Submit Button is clicked.")


                 X_button = WebDriverWait(driver, 10).until(
                 EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div/div/div/button")))
                 X_button.click()  

                 print("X Button is clicked.")
            
                 time.sleep(10)
   
             except TimeoutException:
                 print("Form elements not found on the page")
                 return
        

        driver.refresh()  

        # Short delay to ensure page loads completely
        time.sleep(5)

        # Print the title and URL after navigating to the form page
        print(f"Page title on form page: {driver.title}")
        print(f"Current URL on form page: {driver.current_url}")

    def tearDown(self):
       self.driver.quit()

if __name__ == '__main__':
    unittest.main()
