using OpenQA.Selenium;
using OpenQA.Selenium.Support.UI;
using SeleniumExtras.WaitHelpers;

namespace autotests.Pages
{
    public class GoogleSignupPage
    {
        private readonly IWebDriver _driver;
        private readonly WebDriverWait _wait;

        private readonly By _firstNameInput = By.Id("firstName");
        private readonly By _lastNameInput = By.Id("lastName");
        private readonly By _dayInput = By.Id("day");
        private readonly By _monthDropdown = By.Id("month");
        private readonly By _yearInput = By.Id("year");
        private readonly By _genderDropdown = By.Id("gender");
        private readonly By _createGmailOption = By.XPath("//div[contains(text(),'Створити власну адресу Gmail')]");
        private readonly By _usernameInput = By.Name("Username");
        private readonly By _nextButton = By.XPath("//span[text()='Далі']/parent::button");

        public GoogleSignupPage(IWebDriver driver)
        {
            _driver = driver;
            _wait = new WebDriverWait(_driver, TimeSpan.FromSeconds(15));
        }

        public void Open()
        {
            _driver.Navigate().GoToUrl("https://accounts.google.com/signup");
        }

        public void FillNameDetails(string firstName, string lastName)
        {
            _wait.Until(ExpectedConditions.ElementExists(_firstNameInput)).SendKeys(firstName);
            _driver.FindElement(_lastNameInput).SendKeys(lastName);
            ClickNextButton();
        }
        
        public void FillDateOfBirth(string day, string month, string year)
        {
            _wait.Until(ExpectedConditions.ElementExists(_dayInput)).SendKeys(day);
            _driver.FindElement(_yearInput).SendKeys(year);

            var monthDropdown = _wait.Until(ExpectedConditions.ElementToBeClickable(_monthDropdown));
            monthDropdown.Click();
            var monthOption = _wait.Until(ExpectedConditions.ElementToBeClickable(
                By.XPath($"//span[contains(text(),'{month}')]")));
            ((IJavaScriptExecutor)_driver).ExecuteScript("arguments[0].click();", monthOption);
        }

        public void SelectGender(string gender)
        {
            var genderDropdown = _wait.Until(ExpectedConditions.ElementToBeClickable(_genderDropdown));
            genderDropdown.Click();
            var genderOption = _wait.Until(ExpectedConditions.ElementToBeClickable(
                By.XPath($"//span[contains(text(), '{gender}')]")));
            ((IJavaScriptExecutor)_driver).ExecuteScript("arguments[0].click();", genderOption);
            ClickNextButton();
        }

        public void CreateEmail(string username)
        {
            _wait.Until(driver => driver.FindElement(_createGmailOption)).Click();
            _driver.FindElement(_usernameInput).SendKeys(username);
            ClickNextButton();
        }        

        private void ClickNextButton()
        {
            _driver.FindElement(_nextButton).Click();
        }
    }
}