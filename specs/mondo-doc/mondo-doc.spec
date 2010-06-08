# $Id$
# Authority: dag

Summary: Documentation for Mondo Rescue
Name: mondo-doc
Version: 2.2.8
Release: 1%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://www.mondorescue.org/

Source: ftp://ftp.mondorescue.org/src/mondo-doc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: docbook-utils

%description
Documentation for Mondo Rescue

%prep
%setup

%build
%{__make} -f Makefile.man VERSION="%{version}"
%{__make} -f Makefile.howto VERSION="%{version}"

%install
%{__rm} -rf %{buildroot}
%{__make} -f Makefile.man install INSTALLDIR="%{buildroot}%{_docdir}/%{name}-%{version}"
%{__make} -f Makefile.howto install INSTALLDIR="%{buildroot}%{_docdir}/%{name}-%{version}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_docdir}/%{name}-%{version}/

%changelog
* Tue Jun 08 2010 Dag Wieers <dag@wieers.com> - 2.2.8-1
- Initial package. (using DAR)
