# $Id$
# Authority: dag
# Upstream: Adam Kennedy <adamk@cpan.org>
# ExcludeDist: el4  [because of perl(List::Util) >= 1.18]

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Perl-MinimumVersion

Summary: Find a minimum required version of perl for Perl code
Name: perl-Perl-MinimumVersion
Version: 1.22
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Perl-MinimumVersion/

Source: http://www.cpan.org/modules/by-module/Perl/Perl-MinimumVersion-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Find::Rule) >= 0.30
BuildRequires: perl(File::Find::Rule::Perl) >= 1.04
BuildRequires: perl(File::Spec) >= 0.80
BuildRequires: perl(List::Util) >= 1.18
BuildRequires: perl(PPI) >= 1.205
BuildRequires: perl(Params::Util) >= 0.25
BuildRequires: perl(Perl::Critic::Utils) >= 1.104
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(Test::Script) >= 1.03
BuildRequires: perl >= 5.005
BuildRequires: perl(version) >= 0.76
Requires: perl(File::Find::Rule) >= 0.30
Requires: perl(File::Find::Rule::Perl) >= 1.04
Requires: perl(List::Util) >= 1.18
Requires: perl(PPI) >= 1.205
Requires: perl(Params::Util) >= 0.25
Requires: perl(Perl::Critic::Utils) >= 1.104
Requires: perl >= 5.005
Requires: perl(version) >= 0.76

%filter_from_requires /^perl*/d
%filter_setup

%description
Find a minimum required version of perl for Perl code.

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
%doc %{_mandir}/man1/perlver.1*
%doc %{_mandir}/man3/Perl::MinimumVersion.3pm*
%{_bindir}/perlver
%dir %{perl_vendorlib}/Perl/
#%{perl_vendorlib}/Perl/MinimumVersion/
%{perl_vendorlib}/Perl/MinimumVersion.pm

%changelog
* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 1.22-1
- Updated to version 1.22.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.20-1
- Updated to version 1.20.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.15-1
- Initial package. (using DAR)
