# $Id$
# Authority: dries
# Upstream: "David L. Parsley" <parsley$linuxjedi,org>

Summary: Dhcp/omapi tool for operating on a running dhcp server
Name: omcmd
Version: 0.4.7
Release: 3%{?dist}
License: GPL
Group: Applications/Internet
URL: http://peregrin.jmu.edu/~parsledl/

Source: http://peregrin.jmu.edu/~parsledl/omcmd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: dhcp-devel

%description
omcmd is a CLI utility for querying and updating omapi objects in a running
ISC dhcp server. It can be used to dynamically create/modify/remove/lookup
hosts and leases.

%prep
%setup

%build
%{__make} clean
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 omcmd %{buildroot}%{_bindir}/omcmd
%{__install} -Dp -m0644 omcmd.1 %{buildroot}%{_mandir}/man1/omcmd.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog COPYING README TODO
%doc %{_mandir}/man1/omcmd.1*
%{_bindir}/omcmd

%changelog
* Mon Feb 12 2007 Dries Verachtert <dries@ulyssis.org> - 0.4.7-3
- Fix: first remove the binaries, thanks to Sander Steffann.

* Mon Jan 09 2007 Dag Wieers <dag@wieers.com> - 0.4.7-2
- Added TODO and man-page.
- Fixed Source and URL.

* Mon Jan 08 2007 Dries Verachtert <dries@ulyssis.org> - 0.4.7-1
- Updated to release 0.4.7.

* Tue Oct 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.4.6-1
- Updated to release 0.4.6.

* Sun Aug 08 2004 Dag Wieers <dag@wieers.com> - 0.4.3-1
- Added summary/description from David's package. (David L. Parsley)

* Fri Aug 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.4.3-1
- Initial package.
