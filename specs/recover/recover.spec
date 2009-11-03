%define name recover
%define version 1.3c
%define release 3%{?dist}
%define prefix %{_prefix}
%define summary Utility for recovering a lost file

Summary: Tool to recover lost files
Name: recover
Version: 1.3c
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://recover.sourceforge.net/linux/recover/

Source: recover-%{version}.tar.bz2
Patch: recover-1.3c.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

requires: e2fsprogs

%description
Recover is a utility which automates some steps as described in the
Ext2fs-Undeletion howto. http://pobox.com/~aaronc/tech/e2-undel/howto.txt)
in order to recover lost files.

%prep
%setup
%patch

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE README
%doc %{_mandir}/man1/recover.1*
%{_bindir}/recover
%{_datadir}/recover/

%changelog
* Sun Nov 09 2008 Dag Wieers <dag@wieers.com> - 1.3c-1
- Initial package. (using DAR)
