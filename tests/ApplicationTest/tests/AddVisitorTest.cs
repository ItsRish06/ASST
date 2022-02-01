using NUnit.Framework;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace ApplicationTest.tests
{
    public class AddVisitorTest:BaseTest
    {
        [Test]
        public void VerifyAddKnowVisitor()
        {
            extentReportUtils.createTestCase("Add Visitor Function Test");
            extentReportUtils.addTestLog(AventStack.ExtentReports.Status.Info, "Verifying add known visitor functionality");
            bool result = addVisitor.addKnownVisitor("Rishab Shetty", "32");

            Assert.IsTrue(result);

            
        }
    }
}
