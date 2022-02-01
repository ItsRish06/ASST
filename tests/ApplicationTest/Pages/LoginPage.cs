using ApplicationTest.Pages;
using OpenQA.Selenium;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ApplicationTest.Pages
{
    public class LoginPage : BasePage
    {
        private IWebDriver _driver;

        private IWebElement email => _driver.FindElement(By.Id("id_email"));

        private IWebElement password => _driver.FindElement(By.Id("id_pass"));

        private IWebElement loginBtn => _driver.FindElement(By.ClassName("form__btn"));

        public LoginPage(IWebDriver driver)
        {
            _driver = driver;
        }

        public void LoginToApplication(string sUsername,string sPassword)
        {
            cmnElement.SetText(email, sUsername);
            cmnElement.SetText(password, sPassword);
            cmnElement.ClickElement(loginBtn);
        }




    }
}
