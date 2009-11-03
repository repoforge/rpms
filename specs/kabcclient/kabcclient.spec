# $Id$
# Authority: dries
# Upstream: Kevin Krammer <kevin,krammer$gmx,at>

Summary: Command line access to the KDE address book
Name: kabcclient
Version: 0.8.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://www.sbox.tugraz.at/home/v/voyager/kabcclient/index.html

Source: http://www.sbox.tugraz.at/home/v/voyager/kabcclient/kabcclient-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gcc-c++

%description
KABC Client is a command line tool that provides access to the KDE address
book, which is also used by applications like KAddressBook. It can take its
input from either the command line or through standard input, allowing its
use in Unix shell pipe and filter constructs. Input and output text is
interpreted and formatted by filters.

%prep
%setup

%build
qmake
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 bin/kabcclient %{buildroot}%{_bindir}/kabcclient

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README
%{_bindir}/kabcclient

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.1-1.2
- Rebuild for Fedora Core 5.

* Wed Aug 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.8.1-1
- Update to release 0.8.1.

* Mon Aug 29 2005 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Initial package.
