# $Id$
# Authority: dag
# Upstream: Lincoln D. Stein <lstein$cshl,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Interface

Summary: Perl module to access to network card configuration information
Name: perl-IO-Interface
Version: 1.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Interface/

Source: http://www.cpan.org/modules/by-module/IO/IO-Interface-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
IO-Interface is a Perl module to accessto network card
configuration information.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

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
%doc %{_mandir}/man3/IO::Interface.3pm*
%doc %{_mandir}/man3/IO::Interface::Simple.3pm*
%dir %{perl_vendorarch}/auto/IO/
%{perl_vendorarch}/auto/IO/Interface/
%dir %{perl_vendorarch}/IO/
%{perl_vendorarch}/IO/Interface/
%{perl_vendorarch}/IO/Interface.pm

%changelog
* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 1.04-1
- Updated to release 1.04.

* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 1.03-1
- Initial package. (using DAR)
