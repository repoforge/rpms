# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Proc-ProcessTable

Summary: Perl interface to the UNIX process table
Name: perl-Proc-ProcessTable
Version: 0.41
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Proc-ProcessTable/

Source: http://www.cpan.org/modules/by-module/Proc/Proc-ProcessTable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module is a first crack at providing a consistent interface to
Unix (and maybe other multitasking OS's) process table information.
The impetus for this came about with my frustration at having to parse
the output of various systems' ps commands to check whether specific
processes were running on different boxes at a larged mixed UNIX site.
The output format of ps was different on each OS, and sometimes
changed with each new release of an OS. Also, running a ps subprocess
from within a perl or shell script and parsing the output was not a
very efficient or aesthetic way to do things.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes PORTING README* TODO
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/Proc/
%{perl_vendorarch}/Proc/example.pl
%{perl_vendorarch}/Proc/Killall.pm
%{perl_vendorarch}/Proc/Killfam.pm
%{perl_vendorarch}/Proc/ProcessTable/
%{perl_vendorarch}/Proc/ProcessTable.pm
%dir %{perl_vendorarch}/auto/Proc/
%{perl_vendorarch}/auto/Proc/ProcessTable/

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.41-1
- Updated to release 0.41.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.40-1.2
- Rebuild for Fedora Core 5.

* Sat Nov 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.40-1
- Updated to release 0.40.

* Tue Mar 29 2005 Dag Wieers <dag@wieers.com> - 0.39-1
- Initial package, contributed by Rudolf Kastl.
