# $Id$

# Authority: dag

%define rname Unicode-MapUTF8

Summary: Unicode-MapUTF8 (Conversions to and from arbitrary character sets and UTF8) module for perl.
Name: perl-Unicode-MapUTF8
Version: 1.09
Release: 0
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-MapUTF8/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/S/SN/SNOWHARE/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: perl >= 0:5.8.0
Requires: perl >= 0:5.8.0

%description
Unicode-MapUTF8 (Conversions to and from arbitrary character sets and UTF8) module for perl.

%prep
%setup -n %{rname}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

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
%doc MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/

%changelog
* Wed Jan 21 2004 Dag Wieers <dag@wieers.com> - 1.09-0
- Initial package. (using DAR)
