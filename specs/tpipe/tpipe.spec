# $Id$
# Authority: dag
# Upstream: Juanjo Garcia <juanjo$eurogaran,com>

Summary: Unix command pipeline plumbing tool
Name: tpipe
Version: 1.6
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.eurogaran.com/downloads/tpipe/

Source: http://www.eurogaran.com/downloads/tpipe/tpipe-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
tpipe is a Unix command pipeline plumbing tool. It duplicates standard
input and/or standard ouput.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#makeinstall
%{__install} -Dp -m0755 tpipe %{buildroot}%{_bindir}/tpipe
%{__install} -Dp -m0644 tpipe.1 %{buildroot}%{_mandir}/man1/tpipe.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL README.txt
%doc %{_mandir}/man1/tpipe.1*
%{_bindir}/tpipe

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.6-1.2
- Rebuild for Fedora Core 5.

* Sat Jan 25 2004 Dag Wieers <dag@wieers.com> - 1.6-1
- Initial package. (using DAR)
