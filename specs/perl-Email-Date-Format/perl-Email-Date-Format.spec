# $Id$
# Authority: dag
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Date-Format

Summary: Produce RFC 8822 date strings
Name: perl-Email-Date-Format
Version: 1.002
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Date-Format/

Source: http://www.cpan.org/modules/by-module/Email/Email-Date-Format-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Produce RFC 8822 date strings.

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
%doc %{_mandir}/man3/Email::Date::Format.3pm*
%dir %{perl_vendorlib}/Email/
%dir %{perl_vendorlib}/Email/Date/
#%{perl_vendorlib}/Email/Date/Format/
%{perl_vendorlib}/Email/Date/Format.pm

%changelog
* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 1.002-1
- Initial package. (using DAR)
