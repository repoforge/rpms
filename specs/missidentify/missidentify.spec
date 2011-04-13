# $Id$
# Authority: dag

Summary: Find Win32 applications
Name: missidentify
Version: 1.0
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://missidentify.sourceforge.net/

Source: http://dl.sf.net/missidentify/missidentify-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Miss Identify is a program to find Win32 applications. In its default
mode it displays the filename of any executable that does not have
an executable extension (i.e. exe, dll, com, sys, cpl, hxs, hxi, olb,
rll, or tlb). The program can also be run to display all executables
encountered, regardless of the extension. This is handy when looking
for all of the executables on a drive. Other options allow the user to
record the strings found in an executable and to work recursively. See
the manual page for more information.
Sample output

Searching for mislabeled executables

   C:\> missidentify *
   C:\missidentify-1.0\sample.jpg

Searching for all executables

   C:\> missidentify -a *
   C:\missidentify-1.0\sample.jpg
   C:\missidentify-1.0\missidentify.exe

Searching for all executables in an unusual place

   C:\> missidentify -ar c:\windows\system32
   ...
   C:\WINDOWS\System32\ntdll.dll
   C:\WINDOWS\System32\ntoskrnl.exe
   C:\WINDOWS\System32\NEVER-GONNA-CATCH-ME.EXE
   C:\WINDOWS\System32\ntver.dll

%prep
%setup

%build
%configure
%{__make} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/missidentify.1*
%{_bindir}/missidentify

%changelog
* Wed Feb 16 2011 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
