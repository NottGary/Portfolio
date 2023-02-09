#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.

WinGet, winId, ID, ahk_class Chrome_WidgetWin_1
WinActivate, ahk_id %winId%
FullName := "Error"
OutputVar := "Email Test"

Run, chrome.exe https://www.linkedin.com/hiring/jobs/3426598034/applicants/12646537236/detail/?r=GOOD_FIT

Sleep, 10000

MouseClick, L, 978, 336

MouseClick, L, 978, 336

MouseClick, L, 978, 336

sleep 300

; Copy the selected text
Send, ^c

; Store the copied text in a variable
ClipWait
StringTrimLeft, FullName, Clipboard, 1
StringTrimRight, FullName, FullName, 1

sleep 500

MouseClick, L, 380, 8 ; clicks on sheets tab
MouseClick, L, 93, 256 ;  clicks on name tab
MouseClick, L, 93, 256 ;  clicks on name tab
Send %FullName%
Sleep, 1531
MouseClick, L, 260, 261 ; clicks on email tab
MouseClick, L, 260, 261 ; clicks on email tab
Send %OutputVar%
Sleep, 1000
MouseClick, L, 137, 8 ; clicks back on linkedin tab

