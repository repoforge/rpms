# $Id$
# Authority: dag
# Upstream: Tony Bowden <tony$tmtm,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-ContextualFetch

Summary: Perl module to add contextual fetches to DBI
Name: perl-DBIx-ContextualFetch
Version: 1.03
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-ContextualFetch/

Source: http://www.cpan.org/modules/by-module/DBIx/DBIx-ContextualFetch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
DBIx-ContextualFetch is a Perl module to add contextual fetches to DBI.

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
%doc %{_mandir}/man3/DBIx::ContextualFetch.3pm*
%dir %{perl_vendorlib}/DBIx/
%{perl_vendorlib}/DBIx/ContextualFetch.pm

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 1.03-1
- Initial package. (using DAR)
