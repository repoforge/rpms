# $Id$
# Authority: dries
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Date

Summary: Find and format date headers
Name: perl-Email-Date
Version: 1.103
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Date/

Source: http://www.cpan.org/modules/by-module/Email/Email-Date-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
With this package you can find and format date headers.

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
%doc %{_mandir}/man3/Email::Date.3pm*
%dir %{perl_vendorlib}/Email/
#%{perl_vendorlib}/Email/Date/
%{perl_vendorlib}/Email/Date.pm

%changelog
* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 1.103-1
- Updated to release 1.103.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.102-1
- Updated to release 1.102.

* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 1.101-1
- Initial package.
