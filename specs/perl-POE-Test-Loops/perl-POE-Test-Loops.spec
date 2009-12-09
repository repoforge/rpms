# $Id$
# Authority: cmr
# Upstream: Ilya Zakharevich <cpan$ilyaz,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Test-Loops

Summary: Perl module named POE-Test-Loops
Name: perl-POE-Test-Loops
Version: 1.030
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Test-Loops/

Source: http://search.cpan.org/CPAN/authors/id/R/RC/RCAPUTO/POE-Test-Loops-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup

%description
eusable tests for POE::Loop autors.

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
%doc %{_mandir}/man3/POE::Test::Loops.3pm*
%doc %{_mandir}/man1/poe-gen-tests.1*
%{perl_vendorlib}/POE/Test
%{perl_vendorlib}/POE/Test/Loops.pm
%{_bindir}/poe-gen-tests

%changelog
* Wed Dec  9 2009 Christoph Maser <cmr@financial.com> - 1.030-1
- Updated to version 1.030.

* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 1.022-1
- Updated to version 1.022.

* Thu Jul 30 2009 Christoph Maser <cmr@financial.com> - 1.021-1
- Initial package. 
