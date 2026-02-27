#define SourceDir "D:\GitHub\MOKO\MOKO_GermanDriver\"
#define AppPublisher "MOKO"
#define AppVersion "4.6.10.2"
#define AppName "GermanDrivers"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same Am nppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{07727925-8a79-4826-8998-5e63f25ab5ea}
AppName={#AppName}
AppVersion={#AppVersion}
; AppVerName={#AppName} {#AppVersion}
AppPublisher={#AppPublisher}
DefaultDirName=C:\MOKO SE\Drivers\
DisableDirPage=auto
DefaultGroupName={#AppPublisher}
DisableProgramGroupPage=auto
LicenseFile="iss\license.txt" 
OutputDir="installer"
OutputBaseFilename=Setup_MOKO_GermanDrivers_{#AppVersion}
SetupIconFile="Icon\MOKO Driver IN.ico" 
Compression=lzma2/ultra64
SolidCompression=yes
DisableFinishedPage=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
;Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"
           

[Files]
Source: "GermanDriverCompiled_DLL\*"; DestDir: "{app}\" ;  Flags: ignoreversion  uninsremovereadonly
Source: "GermanPythonDocs\*"; DestDir: "{app}\" ;  Flags: ignoreversion  uninsremovereadonly


[Icons]

[Code]

[Run]














