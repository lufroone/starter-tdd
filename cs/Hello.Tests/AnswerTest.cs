using Shouldly;

namespace Hello.Tests;

public class Tests
{
    private Answer _answer;

    [SetUp]
    public void Setup()
    {
        _answer = new Answer();
    }

    [Test]
    public void TestGetAnswer()
    {
        var actual = _answer.Get();
        actual.ShouldBe(42);
    }
}