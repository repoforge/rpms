# $Id$
# Authority: dag
# Upstream: Rafaël Garcia-Suarez <rgarciasuarez$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Switch

Summary: Perl module that implements a switch statement
Name: perl-Switch
Version: 2.14
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Switch/

Source: http://www.cpan.org/authors/id/R/RG/RGARCIA/Switch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Switch is a Perl module that implements a switch statement.

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
%doc %{_mandir}/man3/Switch.3pm*
%{perl_vendorlib}/Switch.pm

%changelog
* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 2.14-1
- Updated to version 2.14.

* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 2.13-1
- Initial package. (using DAR)
