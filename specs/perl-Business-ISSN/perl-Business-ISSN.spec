# $Id$
# Authority: dries
# Upstream: Brian D foy <bdfoy$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Business-ISSN

Summary: Work with International Standard Serial Numbers
Name: perl-Business-ISSN
Version: 0.91
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Business-ISSN/

Source: http://www.cpan.org/modules/by-module/Business/Business-ISSN-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Work with International Standard Serial Numbers.

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
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Business::ISSN.3pm*
%dir %{perl_vendorlib}/Business/
#%{perl_vendorlib}/Business/ISSN/
%{perl_vendorlib}/Business/ISSN.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.91-1
- Updated to release 0.91.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.90-1
- Initial package.
