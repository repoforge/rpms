# $Id: $

# Authority: dries
# Upstream: 

Summary: Mother of all Gravity Games
Name: moagg
Version: 0.8
Release: 1
License: GPL
Group: Amusements/Games
URL: http://moagg.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/moagg/moagg-%{version}-src.tar.bz2
Source1: http://dl.sf.net/moagg/moagg-%{version}-data.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root

# Screenshot: http://moagg.sourceforge.net/screenshots/blackhole.png
# ScreenshotURL: http://moagg.sourceforge.net/screenshots.php

%description

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%files
%defattr(-,root,root, 0755)
%doc

%changelog
* Mon Apr 26 2004 Dries Verachtert <dries@ulyssis.org> 0.8-1
- Initial package
