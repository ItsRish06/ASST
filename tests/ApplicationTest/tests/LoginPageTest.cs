using AventStack.ExtentReports;
using CommonLibs.Implementation;
using NUnit.Framework;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;



namespace ApplicationTest.tests
{
    public class LoginPageTest:BaseTest
    {

        [Test]
        public void VerifyLoginTest()
        {
            extentReportUtils.createTestCase("Verify login tests with valid creds");
            extentReportUtils.addTestLog(Status.Info, "Performing Login");
            loginPage.LoginToApplication("rishab@email.com", "abcd");

            string expectedResult = "Dashboard";
            string actualResult = CmnDriver.GetTitle();

            Assert.AreEqual(expectedResult, actualResult);
        }

        [Test]
        public void VerifyLoginWithInvalidDataTest()
        {
            extentReportUtils.createTestCase("Verify login test with invalid creds");
            extentReportUtils.addTestLog(Status.Info, "Performing Login");
            loginPage.LoginToApplication("rishab1@email.com", "abcd1");

            string expectedResult = "Dashboard";
            string actualResult = CmnDriver.GetTitle();

            Assert.AreNotEqual(expectedResult, actualResult);
        }

    }
}
