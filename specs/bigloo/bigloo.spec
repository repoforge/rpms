# $Id: $

# Authority: dries

Summary: Compiler for the Scheme programming language
Name: bigloo
Version: 2.6d
Release: 1
License: todo
Group: Development/Languages
URL: http://www-sop.inria.fr/mimosa/fp/Bigloo/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: ftp://ftp-sop.inria.fr/mimosa/fp/Bigloo/bigloo%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README

%changelog
* Sat Mar 20 2004 Dries Verachtert <dries@ulyssis.org> 2.6c-1
- Initial package
