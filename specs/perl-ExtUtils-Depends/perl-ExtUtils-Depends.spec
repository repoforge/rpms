# Authority: dag

# Upstream: <gtk-perl-list@gnome.org>

%define rname ExtUtils-Depends

Summary: ExtUtils-Depends module for perl.
Name: perl-ExtUtils-Depends
Version: 0.103
Release: 0
License: LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-Depends/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/gtk2-perl/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
BuildRequires: perl >= 0:5.8.0
Requires: perl >= 0:5.8.0

%description
This module tries to make it easy to build Perl extensions that use functions
and typemaps provided by other perl extensions. This means that a perl
extension is treated like a shared library that provides also a C and an XS
interface besides the perl one.  This works as long as the base extension is
loaded with the RTLD_GLOBAL flag (usually done with a sub dl_load_flags {0x01}
in the main .pm file) if you need to use functions defined in the module.

%prep
%setup -n %{rname}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/

%changelog
* Sat Oct 11 2003 Dag Wieers <dag@wieers.com> - 0.103-0
- Updated to release 0.103.

* Sun Jul 20 2003 Dag Wieers <dag@wieers.com> - 0.102-0
- Initial package. (using DAR)
