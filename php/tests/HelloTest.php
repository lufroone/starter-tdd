<?php declare(strict_types=1);
require('src/Hello.php');
use PHPUnit\Framework\TestCase;

class HelloTest extends TestCase {
    public function testItWorks() {
        $hello = new Hello;
        $actual = $hello->getAnswer();
        $this->assertSame($actual, 42);
    }
}
?>
