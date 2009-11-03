# $Id$
# Authority: dag
# Upstream: Tony Bowden <tony$tmtm,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Yada-Yada-Yada

Summary: Perl module to defer coding to later
Name: perl-Yada-Yada-Yada
Version: 1.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Yada-Yada-Yada/

Source: http://www.cpan.org/authors/id/T/TM/TMTM/Yada-Yada-Yada-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Yada-Yada-Yada is a Perl module to defer coding to later.

This package contains the following Perl module:

    Yada::Yada::Yada

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
%doc %{_mandir}/man3/Yada::Yada::Yada.3pm*
%dir %{perl_vendorlib}/Yada/
%dir %{perl_vendorlib}/Yada/Yada/
%{perl_vendorlib}/Yada/Yada/Yada.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
