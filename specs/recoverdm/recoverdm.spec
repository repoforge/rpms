# $Id$
# Authority: dag

Summary: Tool to recover data from damaged disks
Name: recoverdm
Version: 0.19
Release: 2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.vanheusden.com/recoverdm/

Source: http://www.vanheusden.com/recoverdm/recoverdm-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
recoverdm is a tool to help you recover disks with bad sectors. One can
recover files as well as complete devices. If it finds unrecoverable
sectors an empty sector is written to the outputfile and extraction
continues (unlike cat/dd).

While recovering a CD or DVD disk and the program cannot read a sector
cannot be read in "normal mode", then the program tries to read it in
the "RAW mode" (without error-checking etc).

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 mergebad %{buildroot}%{_bindir}/mergebad
%{__install} -Dp -m0755 recoverdm %{buildroot}%{_bindir}/recoverdm
%{__install} -Dp -m0644 recoverdm.1 %{buildroot}%{_mandir}/man1/recoverdm.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc license.txt readme.txt
%doc %{_mandir}/man1/recoverdm.1*
%{_bindir}/mergebad
%{_bindir}/recoverdm

%changelog
* Wed Nov 05 2008 Dag Wieers <dag@wieers.com> - 0.19-2
- Included missing mergebad utility.

* Wed Jun 20 2007 Dag Wieers <dag@wieers.com> - 0.19-1
- Initial package. (using DAR)
