# $Id$

# Authority: dag

%define rname FreezeThaw

Summary: FreezeThaw module for perl.
Name: perl-FreezeThaw
Version: 0.43
Release: 0
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/FreezeThaw/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/I/IL/ILYAZ/modules/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
BuildRequires: perl >= 0:5.8.0
Requires: perl >= 0:5.8.0

%description
FreezeThaw module for perl.

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
* Fri Jul 18 2003 Dag Wieers <dag@wieers.com> - 0.43-0
- Initial package. (using DAR)
