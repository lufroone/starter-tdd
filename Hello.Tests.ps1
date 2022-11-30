. ".\Hello.ps1"

Describe 'Get-Anwser' {
    It 'gets the anwer' {
        Get-Answer | Should -Be 42
    }
}