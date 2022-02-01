using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Edge;
using System;

namespace CommonLibs.Implementation
{
    public class CommonDriver
    {
        public IWebDriver Driver { get; private set; }
        public int PageLoadTimeout { private get; set; }
        public int ElementDetectionTimeout { private get; set; }

        private int _pageLoadTimeout;
        private int _elementDetectionTimeout;

        public CommonDriver(string browserType)
        {
            browserType = browserType.ToLower().Trim();
            _pageLoadTimeout = 10;
            _elementDetectionTimeout = 10;

            if (browserType.Equals("chrome"))
            {
                Driver = new ChromeDriver();
            }else if (browserType.Equals("edge"))
            {
                Driver = new EdgeDriver();
            }
            else
            {
                throw new Exception("Invalid browser type : "+browserType);
            }
        }

        public void NavigateToUrl(string url)
        {
            url = url.Trim();
            Driver.Manage().Timeouts().PageLoad = TimeSpan.FromSeconds(_pageLoadTimeout);
            Driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(_elementDetectionTimeout);
            Driver.Url = url;
        }

        public void CloseBrowser()
        {
            if(Driver != null)
            {
                Driver.Close();
            }
        }

        public void CloseAllBrowsers()
        {
            if(Driver != null)
            {
                Driver.Quit();
            }
        }

        public string GetTitle()
        {
            return Driver.Title;
        }
    }
}
