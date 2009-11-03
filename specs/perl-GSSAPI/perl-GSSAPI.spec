# $Id$
# Authority: dag
# Upstream: Achim Grolms <perl$grolmsnet,de>

%{?dtag: %{expand: %%define %dtag 1}}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name GSSAPI

Summary: Perl extension providing access to the GSSAPIv2 library
Name: perl-GSSAPI
Version: 0.26
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GSSAPI/

Source: http://www.cpan.org/authors/id/A/AG/AGROLMS/GSSAPI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(Test::Pod) >= 1.00
BuildRequires: perl(Test::Pod::Coverage) >= 1.04
%{!?_without_krb5:BuildRequires: krb5-devel}
%{?_with_heimdal:BuildRequires: heimdal-devel}

%description
This module gives access to the routines of the GSSAPI library, as
described in rfc2743 and rfc2744 and implemented by the Kerberos-1.2
distribution from MIT.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/GSSAPI.3pm*
%doc %{_mandir}/man3/GSSAPI::*.3pm*
%{perl_vendorarch}/auto/GSSAPI/
%{perl_vendorarch}/GSSAPI/
%{perl_vendorarch}/GSSAPI.pm

%changelog
* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 0.26-1
- Updated to release 0.26.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 0.24-1
- Updated to release 0.24.
- Disabled auto-requires for examples/.

* Wed Aug 16 2006 Dag Wieers <dag@wieers.com> - 0.23-1
- Updated to release 0.23.

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 0.21-1
- Initial package. (using DAR)
