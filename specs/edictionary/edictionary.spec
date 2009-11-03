# $Id$
# Authority: dries
# Upstream: Vishal Verma <vermavee$gmail,com>

Summary: Command line interface to online dictionaries
Name: edictionary
Version: 2.2
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://edictionary.sf.net/

Source: http://dl.sf.net/edictionary/edict-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
Requires: perl

%description
edictionary is a command line interface to online dictionaries.

%prep
%setup -n edict
%{__perl} -pi -e 's|ln -s \$\(prefix\)|ln -s %{_bindir}|g;' Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall prefix=%{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TODO
%{_bindir}/edict
%{_bindir}/ethes

%changelog
* Sat Dec 30 2006 Dries Verachtert <dries@ulyssis.org> - 2.2-1
- Updated to release 2.2.

* Fri Nov 04 2005 Dries Verachtert <dries@ulyssis.org> - 2.1-1
- Initial package.
