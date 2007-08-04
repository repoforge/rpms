# $Id$
# Authority: dag
# Upstream: Andy Lester <andy$petdance,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Tagset

Summary: Perl module that implements data tables useful in parsing HTML
Name: perl-HTML-Tagset
Version: 3.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Tagset/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Tagset-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-HTML-Tagset is a Perl module that implements data tables
useful in parsing HTML.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/HTML::Tagset.3pm*
%dir %{perl_vendorlib}/HTML/
%{perl_vendorlib}/HTML/Tagset.pm

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 3.10-1
- Initial package. (using DAR)
