# $Id: $

# Authority: dries
# Upstream: 

Summary: Display the HTTP headers returned by webservers
Name: furl
Version: 2.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.gumbynet.org.uk/software/furl.html

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

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
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/*

%changelog
* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> - 2.0-1
- Initial package.
