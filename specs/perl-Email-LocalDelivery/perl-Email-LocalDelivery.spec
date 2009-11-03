# $Id$
# Authority: dag
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-LocalDelivery

Summary: Perl module to deliver a piece of email
Name: perl-Email-LocalDelivery
Version: 0.217
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-LocalDelivery/

Source: http://www.cpan.org/modules/by-module/Email/Email-LocalDelivery-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Email-LocalDelivery is a Perl module to deliver a piece of email.

This package contains the following Perl module:

    Email::LocalDelivery

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Email::LocalDelivery.3pm*
%dir %{perl_vendorlib}/Email/
%{perl_vendorlib}/Email/LocalDelivery/
%{perl_vendorlib}/Email/LocalDelivery.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.217-1
- Initial package. (using DAR)
