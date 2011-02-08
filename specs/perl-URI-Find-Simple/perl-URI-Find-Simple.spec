# $Id$
# Authority: dag
# Upstream: Tom Insam <tom$jerakeen,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-Find-Simple

Summary: Perl module to implement a simple interface to URI::Find
Name: perl-URI-Find-Simple
Version: 1.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-Find-Simple/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TOMI/URI-Find-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Test::More)
BuildRequires: perl(URI::Find)
Requires: perl(Test::More)
Requires: perl(URI::Find)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
perl-URI-Find-Simple is a Perl module to implement a simple interface
to URI::Find.

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
%doc MANIFEST META.yml
%doc %{_mandir}/man3/URI::Find::Simple.3pm*
%dir %{perl_vendorlib}/URI/
%dir %{perl_vendorlib}/URI/Find/
#%{perl_vendorlib}/URI/Find/Simple/
%{perl_vendorlib}/URI/Find/Simple.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 1.03-1
- Updated to version 1.03.

* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 1.01-1
- Updated to version 1.01.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.7-1
- Initial package. (using DAR)
