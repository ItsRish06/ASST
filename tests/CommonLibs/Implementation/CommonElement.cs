using OpenQA.Selenium;
using OpenQA.Selenium.Support.UI;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CommonLibs.Implementation
{
    public class CommonElement
    {
        public void ClickElement(IWebElement element)
        {
            element.Click();
        }
        public void ClearText(IWebElement element) => element.Clear();
        public void SetText(IWebElement element, string textToPass) => element.SendKeys(textToPass);
        public bool IsElementDisplayed(IWebElement element) => element.Displayed;
        public bool IsElementSelected(IWebElement element) => element.Selected;
        public bool IsElementEnabled(IWebElement element) => element.Enabled;
        public SelectElement SelectTheElement(IWebElement element)
        {
            return new SelectElement(element); 
        }
    }
}
