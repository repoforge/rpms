# $Id$

# Authority: dag

%define real_name IO-Multiplex

Summary: IO-Multiplex module for perl
Name: perl-IO-Multiplex
Version: 1.08
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Multiplex/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/B/BB/BBB/IO-Multiplex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: perl >= 0:5.8.0
Requires: perl >= 0:5.8.0

%description
IO-Multiplex module for perl.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*/auto/*{,/*}/.packlist

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 1.08-0
- Updated to release 1.08.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 1.04-0
- Initial package. (using DAR)
