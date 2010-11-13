# $Id$
# Authority: dries

### EL6 ships with deltarpm-3.5-0.5.20090913git.el6
# ExclusiveDist: el2 el3 el4 el5

Summary: Create deltas between rpms
Name: deltarpm
Version: 3.3
Release: 2%{?dist}
License: BSD
Group: Applications/System
URL: http://www.novell.com/products/linuxpackages/professional/deltarpm.html

Source: ftp://ftp.suse.com/pub/projects/deltarpm/deltarpm-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bzip2-devel, rpm-devel >= 4.2

%description
A deltarpm contains the difference between an old
and a new version of a rpm, which makes it possible
to recreate the new rpm from the deltarpm and the old
one. You don't have to have a copy of the old rpm,
deltarpms can also work with installed rpms.

%prep
%setup

%build
%{__make} %{?_smp_mflags} prefix="%{_prefix}" mandir="%{_mandir}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" prefix="%{_prefix}" mandir="%{_mandir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE.BSD README
%doc %{_mandir}/man8/applydeltaiso.8*
%doc %{_mandir}/man8/applydeltarpm.8*
%doc %{_mandir}/man8/combinedeltarpm.8*
%doc %{_mandir}/man8/drpmsync.8*
%doc %{_mandir}/man8/makedeltaiso.8*
%doc %{_mandir}/man8/makedeltarpm.8*
%{_bindir}/applydeltaiso
%{_bindir}/applydeltarpm
%{_bindir}/combinedeltarpm
%{_bindir}/drpmsync
%{_bindir}/makedeltaiso
%{_bindir}/makedeltarpm
%{_bindir}/rpmdumpheader

%changelog
* Fri Mar 09 2007 Dag Wieers <dag@wieers.com> - 3.3-2
- Fixed group.

* Sat Dec 03 2005 Dries Verachtert <dries@ulyssis.org> - 3.3-1
- Initial package.
