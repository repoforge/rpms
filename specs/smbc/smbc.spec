# $Id: $

# Authority: dries

Summary: Text mode SMB (Samba) commander
Name: smbc
Version: 0.7.3
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.rafim.prv.pl/smbc/smbc/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Source: http://www.air.rzeszow.pl/smbc/smbc/%{version}/smbc-%{version}.tgz

%description
Smbc is a program for browsing a local SMB (Samba) network. With smbc, you
can download and upload files or directories and create remote and local
directories. Smbc has a resume function and supports UTF-8 characters.

# Screenshot: http://www.air.rzeszow.pl/smbc/smbc/screenshots/mainpage.jpg
# ScreenshotURL: http://www.air.rzeszow.pl/smbc/smbc/screenshots/

%prep
%{__rm} -rf %{buildroot}
%setup -n smbc

%build
%{__make} %{?_smp_mflags}

%install
%makeinstall

%files
%defattr(-,root,root,0755)


%changelog
* Mon May 24 2004 Dries Verachtert <dries@ulyssis.org> 0.7.3-1
- Initial package
