# $Id$
# Authority: dag
# Upstream: Tatsuhiko Miyagawa <miyagawa$bulknews,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Valid-Loose

Summary: Email::Valid which allows dot before at mark
Name: perl-Email-Valid-Loose
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Valid-Loose/

Source: http://www.cpan.org/modules/by-module/Email/Email-Valid-Loose-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Email::Valid which allows dot before at mark

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
%doc %{_mandir}/man3/Email::Valid::Loose.3pm*
%dir %{perl_vendorlib}/Email/
%dir %{perl_vendorlib}/Email/Valid/
#%{perl_vendorlib}/Email/Valid/Loose/
%{perl_vendorlib}/Email/Valid/Loose.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
