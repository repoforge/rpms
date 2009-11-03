# $Id$
# Authority: dag
# Upstream: Evilio José del Río Silván <edelrio$cmima,csic,es>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-Browse

Summary: Perl module to browse tables
Name: perl-DBIx-Browse
Version: 2.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-Browse/

Source: http://www.cpan.org/modules/by-module/DBIx/DBIx-Browse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-DBIx-Browse is a Perl module to browse tables.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST README examples/
%doc %{_mandir}/man3/DBIx::Browse.3pm*
%doc %{_mandir}/man3/DBIx::Browse::CGI.3pm*
%dir %{perl_vendorlib}/DBIx/
%{perl_vendorlib}/DBIx/Browse/
%{perl_vendorlib}/DBIx/Browse.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 2.09-1
- Initial package. (using DAR)
