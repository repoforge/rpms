# $Id: $

# Authority: dries
# Upstream:

Summary: Dutch online dictionary
Name: gnuvd
Version: 1.0beta4
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.djcbsoftware.nl/projecten/gnuvd/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.djcbsoftware.nl/projecten/gnuvd/gnuvd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

# Screenshot: http://www.djcbsoftware.nl/projecten/gnuvd/gnuvd1.png

%description
A program which searches Dutch words in the online dictionary Van Dale.

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
%defattr(-,root,root, 0755)
%doc README

%changelog
* Sat May 5 2004 Dries Verachtert <dries@ulyssis.org> 1.0beta4
- initial package
