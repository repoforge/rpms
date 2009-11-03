# $Id$
# Authority: dag

Summary: Rescue the still-readable data from a damaged harddisk
Name: myrescue
Version: 0.9.4
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://myrescue.sourceforge.net/

Source: http://dl.sf.net/myrescue/myrescue-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
myrescue is a program to rescue the still-readable data from a
damaged harddisk. It is similar in purpose to dd_rescue, but it
tries to quickly get out of damaged areas to first handle the
not yet damaged part of the disk and return later.

%prep
%setup

%build
%{__make} %{?_smp_mflags} -C src

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/myrescue %{buildroot}%{_bindir}/myrescue
%{__install} -Dp -m0644 doc/myrescue.1 %{buildroot}%{_mandir}/man1/myrescue.1
%{__install} -Dp -m0644 doc/myrescue.de.1 %{buildroot}%{_mandir}/de/man1/myrescue.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%doc %{_mandir}/man1/myrescue.1*
%doc %{_mandir}/de/man1/myrescue.1*
%{_bindir}/myrescue

%changelog
* Thu Nov 01 2007 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Initial package. (using DAR)
