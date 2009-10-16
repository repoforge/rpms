# $Id$
# Authority: dag
# Upstream: Adam Kennedy <adamk@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Script

Summary: Cross-platform basic tests for scripts
Name: perl-Test-Script
Version: 1.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Script/

Source: http://www.cpan.org/modules/by-module/Test/Test-Script-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker) 
#BuildRequires: perl(File::Spec) >= 0.80
BuildRequires: perl(IPC::Run3) >= 0.034
BuildRequires: perl(Probe::Perl) >= 0.01
#BuildRequires: perl(Test::Builder) >= 0.32
#BuildRequires: perl(Test::Builder::Tester) >= 1.02
#BuildRequires: perl(Test::More) >= 0.62
BuildRequires: perl(blib)
BuildRequires: perl >= 5.005
#Requires: perl(File::Spec) >= 0.80
Requires: perl(IPC::Run3) >= 0.034
Requires: perl(Probe::Perl) >= 0.01
#Requires: perl(Test::More) >= 0.62
Requires: perl(blib)
Requires: perl >= 5.005

%filter_from_requires /^perl*/d
%filter_setup

%description
Cross-platform basic tests for scripts.

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
%doc %{_mandir}/man3/Test::Script.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Script.pm

%changelog
* Fri Oct 16 2009 Christoph Maser <cmr@financial.com> - 1.06-1
- Updated to version 1.06.

* Tue Sep 15 2009 Christoph Maser <cmr@financial.com> - 1.05-1
- Updated to version 1.05.

* Mon Mar 03 2008 Dag Wieers <dag@wieers.com> - 1.03-1
- Updated to release 1.03.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 1.02-1
- Initial package. (using DAR)
