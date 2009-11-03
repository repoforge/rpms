# $Id$
# Authority: dag

Summary: Console hex editor
Name: shed
Version: 1.15
Release: 1%{?dist}
License: GPL
Group: Applications/Editors
URL: http://shed.sourceforge.net/

Source: http://dl.sf.net/shed/shed-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
shed is an easy to use hex editor written for unix/linux using ncurses,
with a friendly pico-style interface.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/shed.1*
%{_bindir}/shed

%changelog
* Wed Mar 25 2009 Dag Wieers <dag@wieers.com> - 1.15-1
- Updated to release 1.15.

* Thu Dec 04 2008 Dag Wieers <dag@wieers.com> - 1.14-1
- Updated to release 1.14.

* Tue Jul 11 2006 Dag Wieers <dag@wieers.com> - 1.13-1
- Initial package. (using DAR)
