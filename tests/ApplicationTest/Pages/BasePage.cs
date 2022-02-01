using CommonLibs.Implementation;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ApplicationTest.Pages
{
    public class BasePage
    {
        public CommonElement cmnElement;

        public BasePage()
        {
            cmnElement = new CommonElement();
        }
    }
}
