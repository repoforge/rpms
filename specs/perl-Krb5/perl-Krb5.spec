# $Id$
# Authority: dag
# Upstream: Jeff Horwitz <jeff$smashing,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Krb5

Summary: Perl module that authenticates using Kerberos 5
Name: perl-Krb5
Version: 1.9
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Krb5/

Source: http://search.cpan.org/CPAN/authors/id/J/JH/JHORWITZ/Krb5-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: krb5-devel
BuildRequires: openssl-devel
BuildRequires: perl

%description
perl-Krb5 is a Perl module to authenticate using Kerberos 5.

%prep
%setup -n Krb5-%{version}


%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" KRB5_LIBDIR="%{_prefix}/kerberos/lib" KRB5_INCDIR="%{_prefix}/kerberos/include"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYRIGHT Changes MANIFEST README TODO
%doc %{_mandir}/man3/Authen::Krb5.3pm*
%dir %{perl_vendorarch}/Authen/
%{perl_vendorarch}/Authen/Krb5.pm
%dir %{perl_vendorarch}/auto/Authen/
%{perl_vendorarch}/auto/Authen/Krb5/

%changelog
* Thu Jan  7 2010 Christoph Maser <cmr@financial.com> - 1.9-1
- Updated to version 1.9.

* Mon Aug 27 2007 Dag Wieers <dag@wieers.com> - 1.6-1
- Initial package. (using DAR)
