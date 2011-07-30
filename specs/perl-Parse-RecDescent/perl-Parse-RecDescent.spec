# $Id$
# Authority: dries
# Upstream: Damian Conway <damian$conway,org>

### EL6 ships with perl-Parse-RecDescent-1.962.2-2.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Parse-RecDescent
%define real_version 1.965001

Summary: Generate Recursive-Descent Parsers
Name: perl-Parse-RecDescent
Version: 1.965.1
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Parse-RecDescent/

Source: http://search.cpan.org/CPAN/authors/id/D/DC/DCONWAY/Parse-RecDescent-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(version)

%description
RecDescent incrementally generates top-down recursive-descent text
parsers from simple yacc-like grammar specifications.

%prep
%setup -n %{real_name}-%{real_version}

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
%doc Changes MANIFEST META.yml README tutorial/
%doc %{_mandir}/man3/Parse::RecDescent.3pm*
%{perl_vendorlib}/Parse/RecDescent.pm

%changelog
* Tue Jul 26 2011 Yury V. Zaytsev <yury@shurup.com> - 1.965.1-2
- RFX'ed on RHEL6.

* Tue Oct 05 2010 Dag Wieers <dag@wieers.com> - 1.965.1-1
- Updated to release 1.965001.
- Added perl(version) BuildRequires.

* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 1.962.2-1
- Updated to version 1.962.2.

* Sun May  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.94-1
- Initial package.
