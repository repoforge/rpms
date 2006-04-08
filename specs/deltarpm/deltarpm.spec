# $Id$
# Authority: dries

Summary: Create deltas between rpms
Name: deltarpm
Version: 3.3
Release: 1.2
License: BSD
Group: Applications/Utilities
URL: http://www.novell.com/products/linuxpackages/professional/deltarpm.html

Source: ftp://ftp.suse.com/pub/projects/deltarpm/deltarpm-3.3.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bzip2-devel

%description
A deltarpm contains the difference between an old
and a new version of a rpm, which makes it possible
to recreate the new rpm from the deltarpm and the old
one. You don't have to have a copy of the old rpm,
deltarpms can also work with installed rpms.

%prep
%setup

%build
%{__make} %{?_smp_mflags} bindir=%{_bindir} mandir=%{_mandir} prefix=%{_prefix}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE.BSD README
%doc %{_mandir}/man8/*
%{_bindir}/applydeltaiso
%{_bindir}/applydeltarpm
%{_bindir}/combinedeltarpm
%{_bindir}/drpmsync
%{_bindir}/makedeltaiso
%{_bindir}/makedeltarpm
%{_bindir}/rpmdumpheader

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.3-1.2
- Rebuild for Fedora Core 5.

* Sat Dec 03 2005 Dries Verachtert <dries@ulyssis.org> - 3.3-1
- Initial package.
