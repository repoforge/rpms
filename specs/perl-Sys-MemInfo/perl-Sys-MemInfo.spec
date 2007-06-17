# $Id$
# Authority: dries
# Upstream: sylvain cresto <scresto%20%5b_at_%5d%20gmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sys-MemInfo

Summary: Get information about memory usage
Name: perl-Sys-MemInfo
Version: 0.4
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sys-MemInfo/

Source: http://search.cpan.org/CPAN/authors/id/S/SC/SCRESTO/Sys-MemInfo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This module return the total amount of free and used physical memory
in bytes in totalmem and freemem variables.

%prep
%setup -n %{real_name}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Sys/MemInfo.pm
%{perl_vendorarch}/auto/Sys/MemInfo/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.4-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.4-1
- Updated to release 0.4.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Initial package.
