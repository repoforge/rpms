# $Id: perl-GD-Graph.spec 120 2004-03-15 17:26:20Z dag $

# Authority: dag

%define rname GDGraph

Summary: Graph plotting module for Perl.
Name: perl-GD-Graph
Version: 1.43
Release: 0
License: LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GDGraph/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/M/MV/MVERB/GDGraph-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: perl >= 0:5.8.0
Requires: perl >= 0:5.8.0

%description
Graph plotting module for Perl.

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
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Mon Mar 15 2004 Dag Wieers <dag@wieers.com> - 1.43-0
- Initial package. (using DAR)
