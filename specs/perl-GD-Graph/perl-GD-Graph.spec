# $Id$

# Authority: dag

%define real_name GDGraph

Summary: Graph plotting module for Perl
Name: perl-GD-Graph
Version: 1.43
Release: 0
License: LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GDGraph/

Source: http://www.cpan.org/modules/by-module/GDGraph/GDGraph-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.8.0
Requires: perl >= 0:5.8.0

%description
Graph plotting module for Perl.

%prep
%setup -n %{real_name}-%{version}

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
