# $Id$
# Authority: dag
# Upstream: Andy Armstrong <andy$hexten,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Simple

Summary: Simple totally OO CGI interface that is CGI.pm compliant
Name: perl-CGI-Simple
Version: 1.112
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Simple/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml requires
BuildRequires: perl(IO::Scalar)
BuildRequires: perl(Test::More)


%description
CGI-Simple is a perl module that implements a CGI.pm compliant CGI interface.

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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/CGI::Simple.3pm*
%doc %{_mandir}/man3/CGI::Simple::*.3pm*
%dir %{perl_vendorlib}/CGI/
%{perl_vendorlib}/CGI/Simple/
%{perl_vendorlib}/CGI/Simple.pm

%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 1.112-1
- Updated to version 1.112.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.106-1
- Updated to release 1.106.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 1.105-1
- Updated to release 1.105.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.103-1

* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 0.080-1
- Initial package. (using DAR)
