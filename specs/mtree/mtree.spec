# $Id$
# Authority: dag

Summary: Map a directory hierarchy
Name: mtree
Version: 2.7
Release: 1%{dist}
License: BSD
Group: System/Base
URL: http://www-db.deis.unibo.it/Mtree/

Source: mtree-%{version}.cvs.tar.bz2
Patch: mtree-3.1-owl-linux.patch
Patch2: mtree-2.7.cvs-alt-getlogin.patch
Patch3: mtree-3.1-owl-fixes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel

%description
mtree compares the file hierarchy rooted in the current
directory against a specification read from the standard input.
Messages are written to the standard output for any files whose
characteristics do not match the specification, or which are
missing from either the file hierarchy or the specification.

%prep
%setup -n %{name}-%{version}.cvs
%patch -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} -C usr.sbin/mtree

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 usr.sbin/mtree/mtree %{buildroot}%{_sbindir}/mtree
%{__install} -Dp -m0644 usr.sbin/mtree/mtree.8 %{buildroot}%{_mandir}/man8/mtree.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man8/mtree.8*
%{_sbindir}/mtree

%changelog
* Wed Apr 13 2011 Dag Wieers <dag@wieers.com> - 2.7-1
- Initial package. (using DAR)
