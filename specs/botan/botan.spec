# $Id$
# Authority: dries

Summary: Library implementing a variety of cryptographic algorithms and formats
Name: botan
Version: 1.4.0
Release: 1
License: Other
Group: System Environment/Libraries
URL: http://botan.randombit.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://botan.randombit.net/files/Botan-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, perl
#BuildRequires: compat-gcc-c++

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
./configure.pl \
	--prefix="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__mv} -vf %{buildroot}%{_docdir}/Botan-%{version} rpm-doc

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc rpm-doc/*
%{_bindir}/*
%{_libdir}/libbotan-*.so

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/botan
%{_libdir}/*.a
%{_libdir}/*.so

%changelog
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
