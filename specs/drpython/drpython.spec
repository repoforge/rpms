# $Id: drpython.spec,v 1.1 2004/03/01 10:03:25 driesve Exp $

# Authority: dries

# NeedsCleanup

# TODO: doesn't contain install stuff


Summary: todo
Name: drpython
Version: 2.1.9
Release: 1
License: GPL
Group: Development/Tools
URL: http://drpython.sf.net

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://prdownloads.sourceforge.net/drpython/%{name}-%{version}.zip
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: wxGTK-devel

#(d) primscreenshot: http://drpython.sourceforge.net/linuxclassbrowser.2.x.jpg
#(d) screenshotsurl: http://drpython.sourceforge.net/screenshots.html

%description
todo

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__make} install-strip

%files
%defattr(-,root,root, 0755)
%doc README

%changelog
* Wed Jan 28 2004 Dries Verachtert <dries@ulyssis.org> 2.1.4-1
- first packaging for Fedora Core 1
