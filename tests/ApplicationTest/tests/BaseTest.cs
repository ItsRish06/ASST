using ApplicationTest.Pages;
using AventStack.ExtentReports;
using CommonLibs.Implementation;
using CommonLibs.utils;
using Microsoft.Extensions.Configuration;
using NUnit.Framework;
using NUnit.Framework.Interfaces;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ApplicationTest.tests
{
    public class BaseTest
    {

        public CommonDriver CmnDriver;

        string url = "https://asst-tech.herokuapp.com/login?next=/";

        public LoginPage loginPage;

        public AddVisitor addVisitor;

        public ExtentReportUtils extentReportUtils;

        string reportFilename;

        string currentSolutionDirectory;

        

        [OneTimeSetUp]
        public void preSetup()
        {
            string workingDirectory = Environment.CurrentDirectory;

            currentSolutionDirectory = Directory.GetParent(workingDirectory).Parent.Parent.Parent.FullName;

            reportFilename = currentSolutionDirectory + "/reports/asstTestReport.html";

            extentReportUtils = new ExtentReportUtils(reportFilename);

        }

        [SetUp]
        public void Setup()
        {
            extentReportUtils.createTestCase("Setup");
            CmnDriver = new CommonDriver("chrome");
            extentReportUtils.addTestLog(Status.Info, "Browser Type - Chrome");
            extentReportUtils.addTestLog(Status.Info, " URL - "+url);

            CmnDriver.NavigateToUrl(url);

            loginPage = new LoginPage(CmnDriver.Driver);
            addVisitor = new AddVisitor(CmnDriver.Driver);

        }

        [TearDown]
        public void Teardown()
        {
            if (TestContext.CurrentContext.Result.Outcome == ResultState.Failure)
            {
                extentReportUtils.addTestLog(Status.Fail, "One or more step failed");
            }
            CmnDriver.CloseAllBrowsers();
        }

        [OneTimeTearDown]
        public void postTearDown()
        {
            extentReportUtils.flushReport();
        }
    }
}
