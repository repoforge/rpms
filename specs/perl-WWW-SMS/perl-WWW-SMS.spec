# $Id$
# Authority: dag
# Upstream: Ivo Marino <eim$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-SMS

Summary: Perl module to send SMS using service provided by free websites
Name: perl-WWW-SMS
Version: 0.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-SMS/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-SMS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-WWW-SMS is a Perl module to send SMS using service provided
by free websites.

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
%doc CHANGELOG ChangeLog README samples/
%doc %{_mandir}/man3/*.3pm*
#%doc %{_mandir}/man3/WWW::SMS.3pm*
#%doc %{_mandir}/man3/WWW::SMS::o2UK.3pm*
%dir %{perl_vendorlib}/Telephone/
%{perl_vendorlib}/Telephone/Number.pm
%dir %{perl_vendorlib}/WWW/
%{perl_vendorlib}/WWW/SMS/
%{perl_vendorlib}/WWW/SMS.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
