# $Id$
# Authority: dag
# Upstream: SADAHIRO Tomoyuki <SADAHIRO$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-Normalize

Summary: Perl module that implements Unicode Normalization Forms
Name: perl-Unicode-Normalize
Version: 1.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-Normalize/

Source: http://www.cpan.org/modules/by-module/Unicode/Unicode-Normalize-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Unicode-Normalize is a Perl module that implements Unicode
Normalization Forms.

This package contains the following Perl module:

    Unicode::Normalize

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.N META.yml README
#%doc %{_mandir}/man3/Unicode::Normalize.3pm*
%dir %{perl_vendorarch}/Unicode/
%{perl_vendorarch}/Unicode/Normalize.pm
%dir %{perl_vendorarch}/auto/Unicode/
%{perl_vendorarch}/auto/Unicode/Normalize/

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.02-1
- Initial package. (using DAR)
