# $Id$
# Authority: dag
# Upstream:  Ben Schluricke <support$pftp,de>

Summary: Port-File-Transfer-Program
Name: pftp
Version: 1.1.6
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.pftp.de/

Source: ftp://metalab.unc.edu/pub/Linux/system/network/file-transfer/pftp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: which

%description
pftp is released under the terms of the GNU General Public License.
It transfers files, directories and data from standard input to any
host on the net running pftp.

%prep
%setup

### FIXME: Fix needed for 64bit systems. (Please fix upstream)
%{__perl} -pi.orig -e 's|/lib /usr/lib|/%{_lib} %{_libdir}|g' Makefile

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1

%makeinstall \
	BINDIR="%{buildroot}%{_bindir}" \
	MANDIR="%{buildroot}%{_mandir}"

%{__install} -Dp -m0644 pftp.conf %{buildroot}%{_sysconfdir}/pftp.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes COPYING INSTALL README TODO
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/pftp.conf
%{_bindir}/pftp

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.6-1.2
- Rebuild for Fedora Core 5.

* Sun Jun 27 2004 Dag Wieers <dag@wieers.com> - 1.1.6-1
- Initial package. (using DAR)
