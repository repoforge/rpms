# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unix-Syslog

Summary: Syslog module for perl
Name: perl-Unix-Syslog
Version: 0.100
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unix-Syslog/

Source: http://www.cpan.org/modules/by-module/Unix/Unix-Syslog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Syslog module for perl

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Artistic Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/Unix/
%{perl_vendorarch}/Unix/Syslog.pm
%dir %{perl_vendorarch}/auto/Unix/
%{perl_vendorarch}/auto/Unix/Syslog/

%changelog
* Tue Mar 29 2005 Dag Wieers <dag@wieers.com> - 0.100-1
- Cosmetic changes.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.100-0
- Updated to release 0.100.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
