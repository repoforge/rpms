# $Id$
# Authority: dag

Summary: Off-The-Record Messaging plugin for GAIM
Name: gaim-otr
Version: 3.0.0
Release: 2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.cypherpunks.ca/otr/

Source: http://www.cypherpunks.ca/otr/gaim-otr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel, gtk2-devel, libgcrypt-devel >= 1.2.0, libgpg-error-devel
BuildRequires: libotr-devel >= 3.0.0, gaim-devel >= 1.0.0, gcc-c++
Requires: gaim-devel >= 1.0.0, libotr >= 3.0.0

Provides: otr-plugin = %{version}
Obsoletes: otr-plugin

%description
This is a gaim plugin which implements Off-the-Record (OTR) Messaging.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags} all

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%dir %{_libdir}/gaim/
%exclude %{_libdir}/gaim/gaim-otr.la
%{_libdir}/gaim/gaim-otr.so

%changelog
* Sun Mar 19 2006 Dries Verachtert <dries@ulyssis.org> - 3.0.0-2
- gcc-c++ buildrequirement added.

* Tue Mar 14 2006 Dag Wieers <dag@wieers.com> - 3.0.0-1
- Initial package. (using DAR)
