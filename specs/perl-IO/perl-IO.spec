# $Id$
# Authority: dag
# Upstream: Graham Barr <gbarr$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO
%define real_version 1.2301

Summary: Perl module to load various IO modules
Name: perl-IO
Version: 1.23.1
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO/

Source: http://www.cpan.org/modules/by-module/IO/IO-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-IO is a Perl module to load various IO modules.

%prep
%setup -n %{real_name}-%{real_version}

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
%doc ChangeLog MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/IO/
%{perl_vendorarch}/IO.pm
%{perl_vendorarch}/auto/IO/

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.2301-1
- Initial package. (using DAR)
