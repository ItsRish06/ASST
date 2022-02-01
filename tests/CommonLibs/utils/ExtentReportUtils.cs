using AventStack.ExtentReports;
using AventStack.ExtentReports.Reporter;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CommonLibs.utils
{
    public class ExtentReportUtils
    {
        private ExtentHtmlReporter extentHtmlReporter;

        private ExtentReports extentReports;

        private ExtentTest extentTest;

        public ExtentReportUtils(string htmlReporterFileName)
        {
            extentHtmlReporter = new ExtentHtmlReporter(htmlReporterFileName); ;
            extentReports = new ExtentReports();
            extentReports.AttachReporter(extentHtmlReporter);
        }

        public void createTestCase(string testCaseName)
        {
            extentTest = extentReports.CreateTest(testCaseName);
        }

        public void addTestLog(Status status, string comment)
        {
            extentTest.Log(status, comment);
        }

        public void flushReport()
        {
            extentReports.Flush();
        }
    }
}
