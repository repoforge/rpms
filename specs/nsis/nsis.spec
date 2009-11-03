# $Id$
# Authority: dag

Summary: Open Source installer build tool for Windows applications
Name: nsis
Version: 2.34
Release: 1%{?dist}
License: zlib/libpng
Group: Development/Tools
URL: http://nsis.sourceforge.net/

Source0: http://dl.sf.net/nsis/nsis-%{version}-src.tar.bz2
Source1: http://dl.sf.net/nsis/nsis-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: scons >= 0.96.93
Requires: nsis-data = %{version}

%description
NSIS (Nullsoft Scriptable Install System) is a professional Open Source
system to create Windows installers. It is designed to be as small and
flexible as possible and is therefore very suitable for Internet distribution.

%prep
%setup -n nsis-%{version}-src

unzip %{SOURCE1}
%{__cp} -auvx %{name}-%{version}/* .

%build
scons PREFIX="%{_prefix}" PREFIX_DEST="%{buildroot}" PREFIX_CONF="%{_sysconfdir}" SKIPSTUBS="all" SKIPPLUGINS="all" SKIPUTILS="Library/RegTool,UIs,Makensisw,zip2exe,MakeLangId,NSIS Menu" SKIPMISC="all" VERSION="%{version}" STRIP="false"

%install
%{__rm} -rf %{buildroot}
scons PREFIX="%{_prefix}" PREFIX_DEST="%{buildroot}" PREFIX_CONF="%{_sysconfdir}" SKIPSTUBS="all" SKIPPLUGINS="all" SKIPUTILS="Library/RegTool,UIs,Makensisw,zip2exe,MakeLangId,NSIS Menu" SKIPMISC="all" VERSION="%{version}" STRIP="false" install

%{__install} -d -m0755 %{buildroot}%{_datadir}/nsis/
cp -fr Bin/ Contrib/ Include/ Menu/ Plugins/ Stubs/ %{buildroot}%{_datadir}/nsis/

### Clean up document root
%{__rm} -rf Docs/StrFunc/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Docs/ Examples/
%config(noreplace) %{_sysconfdir}/nsisconf.nsh
%{_bindir}/GenPat
%{_bindir}/LibraryLocal
%{_bindir}/makensis
%{_datadir}/nsis/
%exclude %{_datadir}/doc/nsis/

%changelog
* Fri Feb 15 2008 Dag Wieers <dag@wieers.com> - 2.34-1
- Initial package. (using DAR)
