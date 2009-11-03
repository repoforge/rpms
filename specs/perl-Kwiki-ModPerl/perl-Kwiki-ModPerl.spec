# $Id$
# Authority: dag
# Upstream: ??? <gugod$gugod,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Kwiki-ModPerl

Summary: Perl module to enable Kwiki to work under mod_perl
Name: perl-Kwiki-ModPerl
Version: 0.09
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Kwiki-ModPerl/

Source: http://www.cpan.org/modules/by-module/Kwiki/Kwiki-ModPerl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Kwiki-ModPerl is a Perl module to enable Kwiki to work under mod_perl.

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
%doc %{_mandir}/man3/Kwiki::ModPerl.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Kwiki/
#%{perl_vendorlib}/Kwiki/ModPerl/
%{perl_vendorlib}/Kwiki/ModPerl.pm

%changelog
* Thu May 03 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
