# $Id$
# Authority: dries

Summary: Compiler for the Scheme programming language
Name: bigloo
Version: 2.9a
Release: 1%{?dist}
License: LGPL/GPL
Group: Development/Languages
URL: http://www-sop.inria.fr/mimosa/fp/Bigloo/

Source: ftp://ftp-sop.inria.fr/mimosa/fp/Bigloo/bigloo%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: sqlite-devel

%description
Bigloo is a Scheme implementation devoted to one goal: enabling Scheme based
programming style where C(++) is usually required. Bigloo attempts to make
Scheme practical by offering features usually presented by traditional
programming languages but not offered by Scheme and functional programming.
Bigloo compiles Scheme modules. It delivers small and fast stand alone
binary executables. Bigloo enables full connections between Scheme and C
programs, between Scheme and Java programs, and between Scheme and C#
programs.

%prep
%setup -n bigloo%{version}

%build
./configure \
	--prefix=/usr \
	--bindir=/usr/bin \
	--libdir=%{_libdir} \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--dotnet=no \
	--jvm=no
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot}
%{__mv} -f %{buildroot}%{_prefix}/doc/bigloo-%{version} rpm-doc
# {__mv} -f %{buildroot}%{_bindir}/afile %{buildroot}%{_bindir}/afile-bigloo
%{__rm} -f %{buildroot}%{_libdir}/libbigloo*.so
for i in _s _u fth_s fth_u gc gc_fth ; do \
  ln -s %{_libdir}/bigloo/libbigloo${i}-%{version}.so %{buildroot}%{_libdir}/libbigloo${i}-%{version}.so
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README rpm-doc/*
%{_bindir}/bglafile
%{_bindir}/bgldepend
%{_bindir}/bgljas
%{_bindir}/bgljfile
%{_bindir}/bglmake
%{_bindir}/bglmco
%{_bindir}/bglmem
%{_bindir}/bglmemrun
%{_bindir}/bglpp
%{_bindir}/bglprof
%{_bindir}/bgltags
%{_bindir}/bigloo
%{_bindir}/bigloo2.9a
%{_libdir}/bigloo
%{_datadir}/info/bigloo*
%exclude %{_datadir}/info/dir
%{_datadir}/man/bigloo.1*
%{_libdir}/libbigloo*

%changelog
* Mon Dec 25 2006 Dries Verachtert <dries@ulyssis.org> 2.9a-1
- Updated to release 2.9a.

* Fri Jun 02 2006 Dries Verachtert <dries@ulyssis.org> 2.8a-1
- Updated to release 2.8a.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.7a-1.2
- Rebuild for Fedora Core 5.

* Thu Dec 01 2005 Dries Verachtert <dries@ulyssis.org> 2.7a-1
- Updated to release 2.7a.

* Fri Jul 01 2005 Dries Verachtert <dries@ulyssis.org> 2.6f-1
- Update to release 2.6f.

* Mon Nov 01 2004 Dries Verachtert <dries@ulyssis.org> 2.6e-1
- Update to release 2.6e.

* Wed Jun 2 2004 Dries Verachtert <dries@ulyssis.org> 2.6d-2
- renamed the file /usr/bin/afile to afile-bigloo to avoid a
  conflict with afile from the package netatalk

* Sat Mar 20 2004 Dries Verachtert <dries@ulyssis.org> 2.6d-1
- Initial package
