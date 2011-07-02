# $Id$
# Authority: dag
# Upstream: Andy Armstrong <andy$hexten,net>

### EL5 ships with Test::Harness version 2.56 (perl-5.8.8-32.el5_5.2 package)
%{?el5:# Tag: rfx}
### EL6 ships with perl-Test-Harness-3.17-115.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Harness

Summary: Run Perl standard test scripts with statistics
Name: perl-Test-Harness
Version: 3.23
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Harness/

Source: http://search.cpan.org/CPAN/authors/id/A/AN/ANDYA/Test-Harness-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Run Perl standard test scripts with statistics.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test
%{__make} %{?_smp_mflags} test

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
%doc Changes Changes-2.64 HACKING.pod MANIFEST META.yml README examples/
%doc %{_mandir}/man1/prove.1*
%doc %{_mandir}/man3/App::Prove.3pm*
%doc %{_mandir}/man3/App::Prove::*.3pm*
%doc %{_mandir}/man3/Test::HACKING.3pm*
%doc %{_mandir}/man3/Test::Harness.3pm*
%doc %{_mandir}/man3/TAP::*.3pm*
%{_bindir}/prove
%dir %{perl_vendorlib}/App/
%{perl_vendorlib}/App/Prove/
%{perl_vendorlib}/App/Prove.pm
%dir %{perl_vendorlib}/Test/
#%{perl_vendorlib}/Test/Harness/
%{perl_vendorlib}/Test/HACKING.pod
%{perl_vendorlib}/Test/Harness.pm
%{perl_vendorlib}/TAP/

%changelog
* Mon May 23 2011 Denis Fateyev <denis@fateyev.com> - 3.23-1
- Tagged with 'rfx' for RHEL5
- Updated to version 3.23.

* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 3.22-1
- Updated to version 3.22.

* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 3.21-1
- Updated to version 3.21.

* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 3.17-1
- Updated to version 3.17.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 3.14-1
- Updated to release 3.14.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 3.10-1
- Updated to release 3.10.

* Sun Feb 17 2008 Dag Wieers <dag@wieers.com> - 3.09-1
- Updated to release 3.09.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 3.07-1
- Updated to release 3.07.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 3.06-1
- Updated to release 3.06.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 3.05-1
- Updated to release 3.05.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 3.04-1
- Updated to release 3.04.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 3.03-1
- Updated to release 3.03.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 3.00-1
- Updated to release 3.00.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 2.64-1
- Initial package. (using DAR)
