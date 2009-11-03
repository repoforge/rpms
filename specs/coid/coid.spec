# $Id$
# Authority: dries
# Upstream: Brano Kemen <cameni$gmail,com>

Summary: Object-oriented networking library
Name: coid
Version: 0.8.5
Release: 1.2%{?dist}
License: GPL/LGPL/MPL
Group: Development/Libraries
URL: http://coid.sourceforge.net/

Source: http://dl.sf.net/coid/coid-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, ncurses-devel

%description
COID is an object-oriented networking library with a tool that automatically
generates a lightweight communication layer directly from a C++ class
declaration. The coidgen tool automatically extracts designated classes
and methods from specified header files and generates a corresponding
client class and host dispatcher. The server library manages networked
and local connections and provides various services to running objects.
The communication layer establishes either remote connection through TCP
or direct (vtable) connection between the client and the server (if they
reside in the same process).

%prep
%setup -n %{name}
%{__perl} -pi -e "s| /etc| %{buildroot}/etc|g;" Makefile

%build
%{__make} %{?_smp_mflags} PREFIXDIR=%{_prefix}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
%makeinstall PREFIXDIR=%{buildroot}%{_prefix} MANDIR=%{buildroot}%{_mandir}/man1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL README
%doc %{_mandir}/man1/coid*
%{_bindir}/coid
%{_bindir}/coidc
%{_bindir}/coidgen
%dir %{_sysconfdir}/coid
%config(noreplace) %{_sysconfdir}/coid/.devconf
%{_libdir}/coid/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.5-1.2
- Rebuild for Fedora Core 5.

* Thu Sep 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.8.5-1
- Initial package.
