# $Id$
# Authority: dag

%define real_version 20050625

Summary: Enhanced NetBSD ftp client
Name: tnftp
Version: 0.0.20050625
Release: 1.2%{?dist}
License: BSD
Group: Applications/Internet
URL: ftp://ftp.netbsd.org/pub/NetBSD/misc/lukemftp/

Source: ftp://ftp.netbsd.org/pub/NetBSD/misc/lukemftp/tnftp-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: libtermcap

%description
tnftp is a port of the NetBSD FTP client to other systems.
tnftp was formerly known as `lukemftp' and was renamed by Luke Mewburn
in February 2003.

%prep
%setup -n %{name}-%{real_version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/ftp %{buildroot}%{_bindir}/tnftp
%{__install} -Dp -m0644 src/ftp.1 %{buildroot}%{_mandir}/man1/tnftp.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README THANKS todo
%doc %{_mandir}/man1/tnftp.1*
%{_bindir}/tnftp

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.20050625-1.2
- Rebuild for Fedora Core 5.

* Sun Sep 18 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.20050625-2
- Rebuild with corrected real_version.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 0.0.20050625-1
- Updated to release 20050625.

* Mon Jan 03 2005 Dag Wieers <dag@wieers.com> - 0.0.20050103-1
- Updated to release 20050103.

* Sat Oct 09 2004 Dag Wieers <dag@wieers.com> - 0.0.20030825-1
- Contributed package by Florin Andrei.
