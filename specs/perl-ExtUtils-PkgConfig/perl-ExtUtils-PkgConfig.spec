# $Id$

# Authority: dag

# Upstream: <gtk-perl-list@gnome.org>

%define rname ExtUtils-PkgConfig

Summary: ExtUtils-PkgConfig module for perl.
Name: perl-ExtUtils-PkgConfig
Version: 1.01
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
This module is a simplistic Perl interface to the pkg-config command-line
utility, for use in the Makefile.PLs used to build Perl modules which wrap
the libraries about which pkg-config knows.

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
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/%{_target_cpu}-linux-thread-multi/
%{__rm} -rf %{buildroot}%{_libdir}/perl5/vendor_perl/*/%{_target_cpu}-linux-thread-multi/

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/

%changelog
* Sat Oct 11 2003 Dag Wieers <dag@wieers.com> - 1.01-0
- Initial package. (using DAR)
