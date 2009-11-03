# $Id$
# Authority: dag
# Upstream: Thomas Sibley <trs$bestpractical,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CSS-Squish

Summary: Perl module to compact many CSS files into one big file
Name: perl-CSS-Squish
Version: 0.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CSS-Squish/

Source: http://www.cpan.org/modules/by-module/CSS/CSS-Squish-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-CSS-Squish is a Perl module to compact many CSS files into one big file.

This package contains the following Perl module:

    CSS::Squish

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
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/CSS::Squish.3pm*
%dir %{perl_vendorlib}/CSS/
#%{perl_vendorlib}/CSS/Squish/
%{perl_vendorlib}/CSS/Squish.pm

%changelog
* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 0.08-1
- Updated to version 0.08.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.07-1
- Updated to release 0.07.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
