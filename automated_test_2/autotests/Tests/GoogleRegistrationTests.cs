using autotests.Pages;
using OpenQA.Selenium;
using autotests.Helpers;

namespace autotests.Tests
{
    public class GoogleRegistrationTests : IDisposable
    {
        private readonly IWebDriver _driver;
        private readonly GoogleSignupPage _signupPage;
        private bool _disposed = false;

        public GoogleRegistrationTests()
        {
            _driver = WebDriverFactory.CreateChromeDriver();
            _signupPage = new GoogleSignupPage(_driver);
        }

        [Fact]
        public void RunGoogleRegistrationTest()
        {
            _signupPage.Open();
            _signupPage.FillNameDetails("Sviat", "Humeniuk");
            _signupPage.FillDateOfBirth("31", "лютий", "2000");
            _signupPage.SelectGender("Чоловік");
            _signupPage.CreateEmail("sviat.humeniuk");
        }

        public void Dispose()
        {
            Dispose(true);
            GC.SuppressFinalize(this);
        }

        protected virtual void Dispose(bool disposing)
        {
            if (_disposed)
            {
                return;
            }

            if (disposing)
            {
                _driver.Quit();
            }

            _disposed = true;
        }
            
    }
}