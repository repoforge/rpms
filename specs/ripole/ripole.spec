# $Id$
# Authority: dag
# Upstream: <pldaniels$pldaniels,com>

Summary: Extracts attachments out of mailpack format emails
Name: ripole
Version: 0.2.0
Release: 1.2%{?dist}
License: BSD
Group: Applications/File
URL: http://www.pldaniels.com/ripole/

Source: http://www.pldaniels.com/ripole/ripole-%{version}.tar.gz
Patch0: ripole-0.1.4-shared.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
ripOLE is a small program/library designed to pull out attachments
from OLE2 data files (ie, MS Office documents).  ripOLE is BSD
licenced meaning that commercial projects can also use the code
without worry of licence costs or legal liabilities.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p0

%build
%{__make} shared static ripole \
	CFLAGS="%{optflags} -fPIC -D_REENTRANT -I." \
	MAJOR="0" \
	MINOR="1" \
	MICRO="4"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 ripole %{buildroot}%{_bindir}/ripole
%{__install} -Dp -m0755 libripole.a %{buildroot}%{_libdir}/libripole.a

%{__install} -Dp -m0755 libripole.so.0.1.4 %{buildroot}%{_libdir}/libripole.so.0.1.4
%{__ln_s} -f libripole.so.0.1.4 %{buildroot}%{_libdir}/libripole.so
%{__ln_s} -f libripole.so.0.1.4 %{buildroot}%{_libdir}/libripole.so.0

%{__install} -d -m0755 %{buildroot}%{_includedir}/ripole/
%{__install} -p -m0644 *.h %{buildroot}%{_includedir}/ripole/


%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG CONTRIBUTORS INSTALL LICENSE README TODO
%{_bindir}/ripole
%{_libdir}/libripole.so*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/ripole/
%{_libdir}/libripole.a
%{_libdir}/libripole.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.0-1.2
- Rebuild for Fedora Core 5.

* Mon Dec 12 2005 Dries Verachtert <dries@ulyssis.org> - 0.2.0-1
- Updated to release 0.2.0.

* Tue Mar 29 2005 Dag Wieers <dag@wieers.com> - 0.1.4-1
- Initial package. (using DAR)
