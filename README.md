# 🛡️ ABAtch-Obfuscator
**ABAtch-Obfuscator** is batch obfuscator on python.
## 🚀 How to use

1. **Download Python**: Install Python version 3.10 or higher.
2. **Clone repo or download as zip**: Download the project and **extract the repo from the zip** (Yes, people often forget to do this, but it is required).
3. **Run start.bat**: Place your batch file in the script folder and run `start.bat`.
---

## 📈 Examples

### Before:
```batch
@echo off
title Hello World
echo.
echo Hello World!
echo.
mkdir C:\Users\Admin\Desktop\HelloWorld
pause

```

### After:
```batch
@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion
set "ААAАAААAАА=AESnRX1p2cXVcT5SPfE4vuQ0DuRENt8UeuKVCthg0GCpm"
set "ААААAАAAAA=2eWZNtTEb5WAh9q3khNAVhy32XjMFqSNfOmD1S55QcNKq"
...
call !AАAАAАAAAА:~8,1!!AАAАAАAAAА:~10,1!!AАAАAАAAAА:~17,1!!АААAАAАAАА:~39,1!!ААААAАAАAА!!АААAАAАAАА:~39,1!!AAAААAAААA:~25,1!!AAAААAAААA:~25,1!

```



## ⚠️ Disclaimer

This tool is created for educational purposes and for protecting proprietary code. The author is not responsible for any misuse or damage caused by this software. Use it at your own risk.

