using OpenQA.Selenium;
using OpenQA.Selenium.Support.UI;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ApplicationTest.Pages
{
    public class AddVisitor:BasePage
    {
        private IWebDriver _driver;

        public LoginPage loginPage;

        private IWebElement knownVisitorName => _driver.FindElement(By.Id("id_name"));

        private IWebElement knownVisitorTemp => _driver.FindElement(By.Id("id_temp"));

        private IWebElement formBtn => _driver.FindElement(By.ClassName("form__btn"));

        private IWebElement visitorCardName => _driver.FindElement(By.XPath("//div[@class='visitor-list']/div[1]/div[1]/span[1]"));

        private IWebElement visitorCardTemp => _driver.FindElement(By.XPath("//div[@class='visitor-list']/div[1]/div[2]/span"));

        private IWebElement addVisitorPage => _driver.FindElement(By.XPath("//ul[@class='side-nav']/li[5]"));

        private IWebElement viewVisitorPage => _driver.FindElement(By.XPath("//ul[@class='side-nav']/li[2]"));

        private IReadOnlyCollection<IWebElement> visitorList => _driver.FindElements(By.XPath("//div[@class='visitor-list']/div")); 

        public AddVisitor(IWebDriver driver)
        {
            _driver = driver;
            loginPage = new LoginPage(_driver);
        }

        public bool addKnownVisitor(string name,string temp)
        {
            loginPage.LoginToApplication("rishab@email.com", "abcd");
            viewVisitorPage.Click();
            var visitorsBeforeAdd = visitorList.Count();
            addVisitorPage.Click();
            var selectName = cmnElement.SelectTheElement(knownVisitorName);
            selectName.SelectByText(name);
            cmnElement.SetText(knownVisitorTemp, "32");
            formBtn.Click();
            viewVisitorPage.Click();
            var visitorsAfterAdd = visitorList.Count();
            
            if(visitorsAfterAdd - visitorsBeforeAdd != 1)
            {
                return false;
            }
            
            if((visitorCardName.Text == name) && (visitorCardTemp.Text.Substring(0,2) == temp ))
            {
                return true;
            }
            else
            {
                return false;
            }


        }
    }
}
