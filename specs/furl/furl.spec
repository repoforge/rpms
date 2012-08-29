# $Id$
# Authority: dries

Summary: Display the HTTP headers returned by webservers
Name: furl
Version: 2.1
Release: 2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.gumbynet.org.uk/software/furl.html

Source: http://www.gumbynet.org.uk/software/furl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# BuildRequires:

%description
A small utility designed to display the HTTP headers returned by web-servers
in response to client requests.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/furl

%changelog
* Wed May 09 2012 Dag Wieers <dag@wieers.com> - 2.1-2
- Cosmetic changes.

* Fri Jun 11 2004 Dries Verachtert <dries@ulyssis.org> - 2.1-1
- Update to version 2.1.

* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> - 2.0-1
- Initial package.
