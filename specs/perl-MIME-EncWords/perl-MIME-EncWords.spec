# $Id$
# Authority: dries
# Upstream: Hatuka*nezumi - IKEDA Soji <hatuka$nezumi,nu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MIME-EncWords

Summary: Deal with RFC-1522 encoded words
Name: perl-MIME-EncWords
Version: 1.011.1
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MIME-EncWords/

Source: http://www.cpan.org/modules/by-module/MIME/MIME-EncWords-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test)
Requires: perl >= 0:5.005

%description
Deal with RFC-1522 encoded words.

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
%doc ARTISTIC Changes MANIFEST META.yml README
%doc %{_mandir}/man3/MIME::EncWords.3pm*
%doc %{_mandir}/man3/MIME::EncWords::JA_JP.3pm*
%dir %{perl_vendorlib}/MIME/
%{perl_vendorlib}/MIME/EncWords/
%{perl_vendorlib}/MIME/EncWords.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.011.1-1
- Updated to version 1.011.1.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.010.101-1
- Updated to release 1.010.101.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 1.002-1
- Updated to release 1.002.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.040-1
- Initial package.
