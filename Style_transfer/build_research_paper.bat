@echo off
setlocal
set "PDFLATEX=%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe"

if not exist "%PDFLATEX%" (
  echo MiKTeX pdflatex was not found at:
  echo %PDFLATEX%
  echo Install MiKTeX and the IEEEtran and markdown packages, then retry.
  exit /b 1
)

"%PDFLATEX%" -interaction=nonstopmode -halt-on-error RESEARCH_PAPER.tex
if errorlevel 1 exit /b %errorlevel%
echo Built RESEARCH_PAPER.pdf
endlocal
