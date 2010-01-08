# $Id$
# Authority: dag
# Upstream: Matt S Trout <perl-stuff@trout.me.uk>
# ExcludeDist: el4  <- inherited by Catalyst::Runtime

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-Session-State-Cookie

Summary: Maintain session IDs using cookies
Name: perl-Catalyst-Plugin-Session-State-Cookie
Version: 0.17
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-Session-State-Cookie/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSTROUT/Catalyst-Plugin-Session-State-Cookie-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Catalyst) >= 5.80005
BuildRequires: perl(Catalyst::Plugin::Session) >= 0.27
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Moose)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
Requires: perl(Catalyst) >= 5.80005
Requires: perl(Catalyst::Plugin::Session) >= 0.27
Requires: perl(MRO::Compat)
Requires: perl(Moose)
Requires: perl(namespace::autoclean)

%filter_from_requires /^perl*/d
%filter_setup


%description
Maintain session IDs using cookies.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Catalyst::Plugin::Session::State::Cookie.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%dir %{perl_vendorlib}/Catalyst/Plugin/Session/
%dir %{perl_vendorlib}/Catalyst/Plugin/Session/State/
#%{perl_vendorlib}/Catalyst/Plugin/Session/State/Cookie/
%{perl_vendorlib}/Catalyst/Plugin/Session/State/Cookie.pm

%changelog
* Fri Jan  8 2010 Christoph Maser <cmr@financial.com> - 0.17-1
- Updated to version 0.17.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
