# $Id$
# Authority: dag
# Upstream: David Muir Sharnoff <muir$idiom,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-SendVarious

Summary: Send mail via STMP and sendmail
Name: perl-Mail-SendVarious
Version: 0.3
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-SendVarious/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-SendVarious-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Send mail via STMP and sendmail.

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
%doc META.yml README
%doc %{_mandir}/man3/Mail::SendVarious.3pm*
%dir %{perl_vendorlib}/Mail/
%{perl_vendorlib}/Mail/SendVarious/
%{perl_vendorlib}/Mail/SendVarious.pm
%{perl_vendorlib}/Mail/SendVarious.pod

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
