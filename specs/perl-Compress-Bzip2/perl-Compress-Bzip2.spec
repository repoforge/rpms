# $Id$
# Authority: dries
# Upstream: David Robins <david_robins$athena_health,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Compress-Bzip2

Summary: Interface to the bzip2 compression library
Name: perl-Compress-Bzip2
Version: 2.09
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Compress-Bzip2/

Source: http://search.cpan.org/CPAN/authors/id/A/AR/ARJAY/Compress-Bzip2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(ExtUtils::MakeMaker), perl, bzip2-devel

%description
Perl-Bzip2 provides Bzip2 bindings for Perl5. I.e. you can use the Bzip2
library from your Perl scripts to compress ordinary Perl strings.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Compress/
%{perl_vendorarch}/Compress/Bzip2.pm
%dir %{perl_vendorarch}/auto/Compress/
%{perl_vendorarch}/auto/Compress/Bzip2/

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.09-1
- Updated to release 2.09.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.08-1
- Updated to release 2.08.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
