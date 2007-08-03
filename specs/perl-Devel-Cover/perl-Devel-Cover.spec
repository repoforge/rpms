# $Id$
# Authority: dag
# Upstream:

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-Cover

Summary: Devel-Cover module for perl
Name: perl-Devel-Cover
Version: 0.61
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-Cover/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-Cover-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Storable), perl(Digest::MD5), perl(Template) >= 2.00
BuildRequires: perl(PPI::HTML) >= 1.07, perl(Tidy) >= 20060719
BuildRequires: perl(Pod::Coverage) >= 0.06, perl(Test::Differences)
Requires: perl

%description
Devel-Cover module for perl.

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
%doc BUGS CHANGES MANIFEST META.yml README TODO
%doc %{_mandir}/man3/Devel::Cover.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Devel/
#%{perl_vendorlib}/Devel/Cover/
%{perl_vendorlib}/Devel/Cover.pm

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.61-1
- Initial package. (using DAR)
