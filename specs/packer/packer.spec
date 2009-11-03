# $Id$
# Authority: dries
# Upstream: Daniel Milstein <dmilstein$users,sf,net>

Summary: Tool that helps in the creation of packages
Name: packer
Version: 0.1.5
Release: 2%{?dist}
License: GPL
Group: Applications/System
URL: http://packer.sourceforge.net/

Source: http://dl.sf.net/packer/packer-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch

%description
Packer is a tool that helps in the creation of packages. It works by asking
the user for information about a program, and then by generating files
needed to create Debian, RPM, Slackware, and Autopackage (distribution
independent installers) packages based off of that information. Unlike
similar tools, it generates files that are of comparable quality to those
that are hand-crafted.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%{__mv} %{buildroot}%{_datadir}/doc/packer rpm-doc

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING rpm-doc/*
%doc %{_mandir}/man1/desktop2menu.1*
%doc %{_mandir}/man1/differ.1*
%doc %{_mandir}/man1/packer.1*
%{_bindir}/desktop2menu
%{_bindir}/differ
%{_bindir}/packer
%{_datadir}/packer/

%changelog
* Fri Mar 09 2007 Dag Wieers <dag@wieers.com> - 0.1.5-2
- Fixed group.

* Sun Feb 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.5-1
- Updated to release 0.1.5.

* Wed Jan 04 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.4-1
- Initial package.
