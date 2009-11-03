# $Id$
# Authority: dries
# Screenshot: http://drpython.sourceforge.net/linuxclassbrowser.2.x.jpg
# ScreenshotURL: http://drpython.sourceforge.net/screenshots.html

Summary: Editor and environment for developing programs in python
Name: drpython
Version: 3.1.3
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://drpython.sourceforge.net/

Source: http://dl.sf.net/drpython/%{name}-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: wxGTK-devel


%description
DrPython is a clean and simple yet powerful and highly customizable
editor/environment for developing programs written in the Python
programming Language.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README

%changelog
* Fri Jul 16 2004 Matthias Saou <http://freshrpms.net/> 3.1.3-1
- Update to 3.1.3.
- Major spec file completing... but nothing near working.

* Wed Jan 28 2004 Dries Verachtert <dries@ulyssis.org> 2.1.4-1
- first packaging for Fedora Core 1

