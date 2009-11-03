# $Id$
# Authority: dries
# Upstream: Steve Hancock <shancock7078$bigfoot,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Perl-Tidy

Summary: Perl module that parses and beautifies perl source
Name: perl-Perl-Tidy
Version: 20090616
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Perl-Tidy/

Source: http://www.cpan.org/modules/by-module/Perl/Perl-Tidy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

Provides: perl-Tidy = %{version}-%{release}
Obsoletes: perl-Tidy  <= %{version}-%{release}

%description
Perltidy is a tool to indent and reformat perl scripts. It can also
write scripts in html format.

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
find docs/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGES COPYING INSTALL MANIFEST META.yml README TODO docs/ examples/
%doc %{_mandir}/man1/perltidy.1*
%doc %{_mandir}/man3/Perl::Tidy.3pm*
%{_bindir}/perltidy
%dir %{perl_vendorlib}/Perl/
#%{perl_vendorlib}/Perl/Tidy/
%{perl_vendorlib}/Perl/Tidy.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 20090616-1
- Updated to version 20090616.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 20071205-1
- Initial package. (using DAR)
