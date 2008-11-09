# $Id$
# Authority: dag

Summary: Off-The-Record Messaging plugin for GAIM
Name: pidgin-otr
Version: 3.2.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.cypherpunks.ca/otr/

Source: http://www.cypherpunks.ca/otr/pidgin-otr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 2.6, gtk2-devel >= 2.6, libgcrypt-devel >= 1.2.0, libgpg-error-devel
BuildRequires: libotr-devel >= 3.0.0, pidgin >= 1.0.0, gcc-c++
Requires: pidgin >= 1.0.0, libotr >= 3.1.0

Obsoletes: otr-plugin <= %{version}-%{release}
Provides: otr-plugin = %{version}-%{release}
Obsoletes: gaim-otr <= %{version}-%{release}
Provides: gaim-otr = %{version}-%{release}

%description
This is a pidgin plugin which implements Off-the-Record (OTR) Messaging.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags} all

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYING README
%dir %{_libdir}/pidgin/
%{_libdir}/pidgin/pidgin-otr.so
%exclude %{_libdir}/pidgin/pidgin-otr.la

%changelog
* Thu Nov 06 2008 Dag Wieers <dag@wieers.com> - 3.2.0-1
- Updated to release 3.2.0.

* Sat Oct 13 2007 Dag Wieers <dag@wieers.com> - 3.1.0-1
- Updated to release 3.1.0.

* Sun Mar 19 2006 Dries Verachtert <dries@ulyssis.org> - 3.0.0-2
- gcc-c++ buildrequirement added.

* Tue Mar 14 2006 Dag Wieers <dag@wieers.com> - 3.0.0-1
- Initial package. (using DAR)
