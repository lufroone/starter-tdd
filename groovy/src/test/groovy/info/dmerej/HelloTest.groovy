package info.dmerej

import spock.lang.Specification

class HelloTest extends Specification {
  def "get answer"() {
    def hello = new Hello()
    def result = hello.getAnswer()

    expect:
    result == 42
  }
}
