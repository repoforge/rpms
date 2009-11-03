# $Id$
# Authority: dries

Summary: Library implementing a variety of cryptographic algorithms and formats
Name: botan
Version: 1.6.4
Release: 1%{?dist}
License: Other
Group: System Environment/Libraries
URL: http://botan.randombit.net/

#Source: http://botan.randombit.net/files/Botan-%{version}.tgz
Source: http://files.randombit.net/botan/archive/v1.6/Botan-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, perl

%description
Botan is a library, written in C++. It's main purpose it to provide an easy
to use, high level interface to various cryptographic primitives, such as
block ciphers, hash functions, and public key algorithms. In addition, the
intent is that Botan is as general purpose as possible, and for this reason,
it supports many standards and de-facto standards.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n Botan-%{version}

%build
%{expand: %%define optflags -O2}
./configure.pl \
	--prefix="%{_prefix}"
%{__perl} -pi -e "s|-o ..OWNER. -g ..GROUP.||g;" Makefile
%{__make} %{?_smp_mflags} LIBDIR=%{_libdir}

%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALLROOT=%{buildroot}%{_prefix} LIBDIR=%{buildroot}%{_libdir}
%{__mv} -vf %{buildroot}%{_docdir}/Botan-%{version} rpm-doc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc rpm-doc/*
%{_bindir}/botan-config
%{_libdir}/libbotan-*.so

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/botan/
%{_libdir}/libbotan.so
%exclude %{_libdir}/libbotan.a

%changelog
* Thu Mar 13 2008 Dries Verachtert <dries@ulyssis.org> - 1.6.4-1
- Updated to release 1.6.4.

* Sun Jul 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.6.3-1
- Updated to release 1.6.3.

* Mon Dec 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.6.0-1
- Updated to release 1.6.0.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.4.12-1.2
- Rebuild for Fedora Core 5.

* Mon Jan 16 2006 Dries Verachtert <dries@ulyssis.org> - 1.4.12-1
- Updated to release 1.4.12.

* Sat Jan 01 2006 Dries Verachtert <dries@ulyssis.org> - 1.4.11-1
- Updated to release 1.4.11.

* Mon Dec 19 2005 Dries Verachtert <dries@ulyssis.org> - 1.4.10-1
- Updated to release 1.4.10.

* Mon Nov 07 2005 Dries Verachtert <dries@ulyssis.org> - 1.4.9-1
- Updated to release 1.4.9.

* Wed Oct 19 2005 Dries Verachtert <dries@ulyssis.org> - 1.4.8-1
- Updated to release 1.4.8.

* Tue Sep 27 2005 Dries Verachtert <dries@ulyssis.org> - 1.4.7-1
- Updated to release 1.4.7.

* Mon Mar 14 2005 Dries Verachtert <dries@ulyssis.org> - 1.4.6-1
- Update to version 1.4.6.

* Sat Dec 04 2004 Dries Verachtert <dries@ulyssis.org> - 1.4.4-1
- Update to version 1.4.4.

* Mon Nov 08 2004 Dries Verachtert <dries@ulyssis.org> - 1.4.3-1
- Update to version 1.4.3.

* Mon Nov 01 2004 Dries Verachtert <dries@ulyssis.org> - 1.4.2-1
- Update to version 1.4.2.

* Fri Oct 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.4.1-1
- Update to version 1.4.1.

* Sat Jun 26 2004 Dries Verachtert <dries@ulyssis.org> - 1.4.0-1
- Update to version 1.4.0.

* Sat Jun 12 2004 Dries Verachtert <dries@ulyssis.org> - 1.3.14-1
- Update to version 1.3.14.

* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.3.13-2
- fix the ownership of the devel files

* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.3.13-1
- Update to 1.3.13

* Fri May 28 2004 Dries Verachtert <dries@ulyssis.org> - 1.2.8-1
- Initial package.
