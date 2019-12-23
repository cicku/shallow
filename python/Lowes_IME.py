#!/usr/bin/python3
"""
IME Spider -- Fetching sales data from IME ReportViewer

Author: Christopher Meng

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

import os
import pathlib
import shutil
import time
import sys
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if sys.version_info[:2] < (3, 7):
    raise SystemExit('Error: Python 3.7 is required!')

download_dir = "C:\IME" # Download folder
driver_path = r"C:\Users\cawk\Desktop\chromedriver.exe" # chromedriver path. make sure Chrome auto update is OFF.
ime_url = 'http://retailerreports.trusthss.com/ReportServer/Pages/ReportViewer.aspx?/Retailer+Reports/ResultsVsPreviousYear_BySourceAffiliateStore&rs:Command=Render'
today = date.today().strftime("%Y-%m-%d") # Today pattern
new_xlsname = 'IME_Lowes_'+today+'.xls' # Name pattern
xlsfiles = os.listdir(download_dir)

class IME_Lowes():
    def main(self):
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument('--incognito')
        options.add_argument('--window-size=400,400')
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option("prefs", {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            'profile.default_content_setting_values.automatic_downloads': 1,
        })
        self.driver = webdriver.Chrome(options=options, executable_path=driver_path)
        self.driver.implicitly_wait(15)
        self.driver.get(ime_url)
        try:
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "ReportViewerControl_ctl04_ctl05_ddValue"))
            )

            # Click actions, sleep() is useful for congestion.
            self.driver.find_element(By.XPATH, "//*[@id='ReportViewerControl_ctl04_ctl05_ddValue']").click()
            WebDriverWait(self.driver, 10)
            dropdown = self.driver.find_element(By.XPATH, "//*[@id='ReportViewerControl_ctl04_ctl05_ddValue']")
            WebDriverWait(self.driver, 10)
            time.sleep(10)
            dropdown.find_element(By.XPATH, "//option[. = 'Lowes']").click()
            WebDriverWait(self.driver, 10)
            self.driver.find_element(By.ID, "ReportViewerControl_ctl04_ctl05_ddValue").click()
            WebDriverWait(self.driver, 10)
            time.sleep(10)
            self.driver.find_element(By.ID, "ReportViewerControl_ctl04_ctl00").click()
            WebDriverWait(self.driver, 10)
            time.sleep(5)
            # Other XPATH are wrong
            self.driver.find_element(By.ID, "ReportViewerControl_ctl05_ctl04_ctl00_ButtonImgDown").click()
            time.sleep(5)
            self.driver.find_element(By.LINK_TEXT, "Excel").click()
            #self.driver.find_element_by_partial_link_text('Excel').click()
            time.sleep(15) # Increase the value if loading takes too long.
        finally:
            self.driver.quit() # Quit before file transaction.

            xls_fp = pathlib.Path(download_dir)
            xls_ts = []
            for x in xls_fp.iterdir():
                xls_ts += [time.strftime('%Y/%m/%d', time.gmtime(os.path.getmtime(x)))]

            for f, t in zip(xlsfiles, xls_ts):
                xlsname, xlsext = os.path.splitext(f)
                # Right now we only have one file per day.
                if xlsname.startswith('ResultsVs') and xlsext == '.xls' and t == date.today().strftime("%Y/%m/%d"):
                    shutil.move(os.path.join(download_dir, f), os.path.join(download_dir, new_xlsname))
                else:
                    pass #TODO rename based on file creation datetime

if __name__ == "__main__":
    IME_Lowes().main()
