# $Id$
# Authority: dag

Summary: General-purpose stream-handling tool
Name: cstream
Version: 2.7.4
Release: 3
License: MIT
Group: Applications/System
URL: http://www.cons.org/cracauer/cstream.html

Source: http://www.cons.org/cracauer/download/cstream-%{version}.tar.gz
Patch2: cstream-2.7.4-Wextra.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
cstream filters data streams, much like the UNIX tool dd(1).

cstream has a more traditional commandline syntax, support for precise
bandwidth limiting and reporting and support for FIFOs.

Data limits and throughput rate calculation will work for files > 4 GB.

%prep
%setup
%patch2 -p1 -b .Wextra

%build
%configure INSTALL="%{__install} -p"
%{__make} %{?_smp_mflags} CFLAGS="%{optflags} -Wall -Wno-unused-parameter -Werror"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYRIGHT README TODO
%doc %{_mandir}/man1/cstream.1*
%{_bindir}/cstream

%changelog
* Fri Feb 08 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 2.7.4-3
- More compile warnings (-Wall -Wextra -Werror).
- Redacted description down to the most important points.

* Fri Feb 08 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 2.7.4-2
- Spec file cleanups (use install target, get rpmlint to shut up).

* Fri Feb 08 2008 Mike Weisenborn <mike@weisenborn.com> - 2.7.4-1
- Initial package
