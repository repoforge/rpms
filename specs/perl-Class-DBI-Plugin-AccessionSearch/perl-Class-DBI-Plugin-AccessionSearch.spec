# $Id$
# Authority: dries
# Upstream: Atsushi Kobayashi <nekokak$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-DBI-Plugin-AccessionSearch

Summary: Plugin for adding search attributes
Name: perl-Class-DBI-Plugin-AccessionSearch
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-DBI-Plugin-AccessionSearch/

Source: http://www.cpan.org/modules/by-module/Class/Class-DBI-Plugin-AccessionSearch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Plugin for adding search attributes.

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
%doc %{_mandir}/man3/Class::DBI::Plugin::AccessionSearch.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/DBI/
%dir %{perl_vendorlib}/Class/DBI/Plugin/
#%{perl_vendorlib}/Class/DBI/Plugin/AccessionSearch/
%{perl_vendorlib}/Class/DBI/Plugin/AccessionSearch.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Updated to release 0.02.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
