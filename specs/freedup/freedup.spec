# $Id$
# Authority: dag

Summary: Reclaim space on your drive
Name: freedup
%define real_version 1.5-3
Version: 1.5.3
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://software.neuper.de/freedup/

Source: http://software.neuper.de/freedup/freedup-%{real_version}-src.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Freedup links identical files to save space. Freedup walks through
one or more file system trees and hardlinks files if the belong to
the same device and symlinks them in case the devices differ and
absolute paths are given.

For files that are generally read from and not written to, this
provides significant space savings particularly to multimedia
content.

%prep
%setup -n %{name}-1.5

%build
%{__make} %{?_smp_mflags} freedup

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 freedup %{buildroot}%{_bindir}/freedup
%{__install} -Dp -m0644 freedup.1 %{buildroot}%{_mandir}/man1/freedup.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING copyright README* TODO html/
%doc %{_mandir}/man1/freedup.1*
%{_bindir}/freedup

%changelog
* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 1.5.3-1
- Updated to release 1.5-3.

* Mon Mar 03 2008 Dag Wieers <dag@wieers.com> - 1.5.2-1
- Updated to release 1.5-2.

* Sun Feb 03 2008 Dag Wieers <dag@wieers.com> - 1.5.1-1
- Updated to release 1.5-1.

* Fri Dec 28 2007 Dag Wieers <dag@wieers.com> - 1.4.3-1
- Updated to release 1.4-3.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 1.4.2-1
- Updated to release 1.4-2.

* Tue Dec 18 2007 Dag Wieers <dag@wieers.com> - 1.3.1-1
- Updated to release 1.3-1.

* Tue Dec 11 2007 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Updated to release 1.2-1.

* Thu Dec 06 2007 Dag Wieers <dag@wieers.com> - 1.1.3-1
- Updated to release 1.1-3.

* Mon Dec 03 2007 Dag Wieers <dag@wieers.com> - 1.1.2-1
- Updated to release 1.1-2.

* Fri Nov 30 2007 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Updated to release 1.1-1.

* Sun Nov 11 2007 Dag Wieers <dag@wieers.com> - 1.0.5-3
- Fix group tag. (really!)

* Sun Nov 11 2007 Dag Wieers <dag@wieers.com> - 1.0.5-2
- Fix group tag.

* Sat Nov 10 2007 Dag Wieers <dag@wieers.com> - 1.0.5-1
- Updated to release 1.0.5.

* Thu Nov 08 2007 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Updated to release 1.0-4.

* Sat Nov 03 2007 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Initial package. (using DAR)
