# $Id$
# Authority: dag
# Upstream: Philip Crow <crow,phil$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UML-State

Summary: Perl module which draws simple state diagrams
Name: perl-UML-State
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UML-State/

Source: http://www.cpan.org/modules/by-module/UML/UML-State-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-UML-State is a Perl module which draws simple state diagrams.

This package contains the following Perl module:

    UML::State

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
find samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README samples/
%doc %{_mandir}/man1/drawstate.pl.1*
%doc %{_mandir}/man1/drawstatexml.pl.1*
%doc %{_mandir}/man3/UML::drawstate.3pm*
%doc %{_mandir}/man3/UML::drawstatexml.3pm*
%doc %{_mandir}/man3/UML::State.3pm*
%{_bindir}/drawstate.pl
%{_bindir}/drawstatexml.pl
%dir %{perl_vendorlib}/UML/
%{perl_vendorlib}/UML/drawstate.pl
%{perl_vendorlib}/UML/drawstatexml.pl
%{perl_vendorlib}/UML/State.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
