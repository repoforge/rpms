# $Id$
# Authority: dag
# Upstream: Philip Guenther <guenther+cpan$sendmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name BIND-Conf_Parser

Summary: Perl module that implements a parser class for BIND configuration files
Name: perl-BIND-Conf_Parser
Version: 0.95
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/BIND-Conf_Parser/

Source: http://www.cpan.org/authors/id/P/PG/PGUEN/BIND-Conf_Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-BIND-Conf_Parser is a Perl module that implements a parser class for BIND
configuration files.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/BIND::Conf_Parser.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/BIND/
#%{perl_vendorlib}/BIND/Conf_Parser/
%{perl_vendorlib}/BIND/Conf_Parser.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.95-1
- Initial package. (using DAR)
