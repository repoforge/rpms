# $Id$
# Authority: dries

Summary: Compiler for the Scheme programming language
Name: bigloo
Version: 2.6d
Release: 2
License: LGPL/GPL
Group: Development/Languages
URL: http://www-sop.inria.fr/mimosa/fp/Bigloo/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: ftp://ftp-sop.inria.fr/mimosa/fp/Bigloo/bigloo%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
	--libdir=/usr/lib \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
	--dotnet=no \
	--jvm=no
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot}
%{__mv} -f %{buildroot}%{_prefix}/doc/bigloo-2.6d rpm-doc
%{__mv} -f %{buildroot}%{_bindir}/afile %{buildroot}%{_bindir}/afile-bigloo

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README rpm-doc/*
%{_bindir}/*
%{_libdir}/bigloo
%{_datadir}/info/bigloo*
%exclude %{_datadir}/info/dir
%{_datadir}/man/bigloo.1*

%changelog
* Wed Jun 2 2004 Dries Verachtert <dries@ulyssis.org> 2.6d-2
- renamed the file /usr/bin/afile to afile-bigloo to avoid a 
  conflict with afile from the package netatalk

* Sat Mar 20 2004 Dries Verachtert <dries@ulyssis.org> 2.6d-1
- Initial package
