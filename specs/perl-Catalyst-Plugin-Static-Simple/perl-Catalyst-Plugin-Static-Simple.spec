# $Id$
# Authority: dag
# Upstream: Matt S Trout <perl-stuff@trout.me.uk>
# ExcludeDist: el4  <- inherited by Catalyst::Runtime

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-Static-Simple

Summary: Make serving static pages painless
Name: perl-Catalyst-Plugin-Static-Simple
Version: 0.29
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-Static-Simple/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSTROUT/Catalyst-Plugin-Static-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Catalyst::Runtime) >= 5.80008
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(MIME::Types) >= 1.25
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
Requires: perl(Catalyst::Runtime) >= 5.80008
Requires: perl(MIME::Types) >= 1.25
Requires: perl(Moose)
Requires: perl(MooseX::Types)
Requires: perl(Test::More)
Requires: perl(namespace::autoclean)

%filter_from_requires /^perl*/d
%filter_setup

%description
Make serving static pages painless.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml 
%doc %{_mandir}/man3/Catalyst::Plugin::Static::Simple.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%dir %{perl_vendorlib}/Catalyst/Plugin/Static/
#%{perl_vendorlib}/Catalyst/Plugin/Static/Simple/
%{perl_vendorlib}/Catalyst/Plugin/Static/Simple.pm

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.29-1
- Updated to version 0.29.

* Fri Jan  8 2010 Christoph Maser <cmr@financial.com> - 0.28-1
- Updated to version 0.28.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.20-1
- Initial package. (using DAR)
