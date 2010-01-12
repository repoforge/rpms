# $Id$
# Authority: dries
# Upstream: Daisuke Komatsu <taro@cpan.org>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-Log-Colorful

Summary: Catalyst Plugin for Colorful Log
Name: perl-Catalyst-Plugin-Log-Colorful
Version: 0.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-Log-Colorful/

Source: http://search.cpan.org/CPAN/authors/id/T/TA/TARO/Catalyst-Plugin-Log-Colorful-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Catalyst::Log)
BuildRequires: perl(Catalyst::Runtime) >= 5.7
BuildRequires: perl(Data::Dumper)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Term::ANSIColor)
BuildRequires: perl(Test::More)
Requires: perl(Catalyst::Log)
Requires: perl(Catalyst::Runtime) >= 5.7
Requires: perl(Data::Dumper)
Requires: perl(MRO::Compat)
Requires: perl(Term::ANSIColor)
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup


%description
Catalyst Plugin for Colorful Log.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Catalyst::Plugin::Log::Colorful.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%dir %{perl_vendorlib}/Catalyst/Plugin/Log/
#%{perl_vendorlib}/Catalyst/Plugin/Log/Colorful/
%{perl_vendorlib}/Catalyst/Plugin/Log/Colorful.pm

%changelog
* Tue Jan 12 2010 Christoph Maser <cmr@financial.com> - 0.15-1
- Updated to version 0.15.

* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 0.12-1
- Updated to release 0.12.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
