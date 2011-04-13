# $Id$
# Authority: dag
# Upstream: Johan Vromans <jv$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Hexify

Summary: Perl extension for hexdumping arbitrary data
Name: perl-Data-Hexify
Version: 1.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Hexify/

Source: http://www.cpan.org/modules/by-module/Data/Data-Hexify-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perl extension for hexdumping arbitrary data.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Data::Hexify.3pm*
%dir %{perl_vendorlib}/Data/
#%{perl_vendorlib}/Data/Hexify/
%{perl_vendorlib}/Data/Hexify.pm

%changelog
* Wed Feb 16 2011 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
