using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;

namespace autotests.Helpers
{
    static class WebDriverFactory
    {
        public static IWebDriver CreateChromeDriver()
        {
            var driver = new ChromeDriver();
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(15);
            return driver;
        }

        public static WebDriverWait CreateWait(IWebDriver driver, int timeoutInSeconds = 15)
        {
            return new WebDriverWait(driver, TimeSpan.FromSeconds(timeoutInSeconds));
        }
    }
}