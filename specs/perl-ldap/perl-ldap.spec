# $Id$

# Authority: dries
# Upstream:

%define real_name perl-ldap
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Interface to LDAP for Perl
Name: perl-ldap
Version: 0.31
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ldap/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/G/GB/GBARR/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
Requires: perl-Convert-ASN1, perl-XML-SAX-Base

%description
This package contains a perl module with an interface to LDAP.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README ChangeLog TODO CREDITS RELEASE_NOTES
%{_mandir}/man3/*
%{perl_vendorlib}/Bundle/Net/LDAP.pm
%{perl_vendorlib}/LWP/Protocol/ldap.pm
%{perl_vendorlib}/Net/LDAP*
%exclude %{perl_vendorarch}/auto/perl-ldap/.packlist
%exclude %{perl_archlib}/perllocal.pod

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Initial package.
