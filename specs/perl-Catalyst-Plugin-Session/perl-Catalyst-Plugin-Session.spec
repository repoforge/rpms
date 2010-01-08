# $Id$
# Authority: dag
# Upstream: Tomas Doran <bobtfish@bobtfish.net>
# ExcludeDist: el4  <- inherited by Catalyst::Runtime


%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-Session

Summary: Generic Session plugin - ties together server side storage and client side state required to maintain session data.  
Name: perl-Catalyst-Plugin-Session
Version: 0.29
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-Session/

Source: http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-Session-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Catalyst::Runtime) >= 5.71001
BuildRequires: perl(Digest)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Moose) >= 0.76
BuildRequires: perl(MooseX::Emulate::Class::Accessor::Fast) >= 0.00801
BuildRequires: perl(Object::Signature)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
#BuildRequires: perl(Tie::RefHash) >= 1.34
BuildRequires: perl(Tie::RefHash)
BuildRequires: perl(namespace::clean) >= 0.10
BuildRequires: perl >= 5.8.0
Requires: perl(Catalyst::Runtime) >= 5.71001
Requires: perl(Digest)
Requires: perl(File::Spec)
Requires: perl(File::Temp)
Requires: perl(MRO::Compat)
Requires: perl(Moose) >= 0.76
Requires: perl(MooseX::Emulate::Class::Accessor::Fast) >= 0.00801
Requires: perl(Object::Signature)
Requires: perl(Test::More)
#Requires: perl(Tie::RefHash) >= 1.34
Requires: perl(Tie::RefHash)
Requires: perl(namespace::clean) >= 0.10
Requires: perl >= 5.8.0

%filter_from_requires /^perl*/d
%filter_setup


%description
Generic Session plugin - ties together server side storage and client side state
required to maintain session data.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Catalyst::Plugin::Session.3pm*
%doc %{_mandir}/man3/Catalyst::Plugin::Session::*.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%{perl_vendorlib}/Catalyst/Plugin/Session/
%{perl_vendorlib}/Catalyst/Plugin/Session.pm

%changelog
* Fri Jan  8 2010 Christoph Maser <cmr@financial.com> - 0.29-1
- Updated to version 0.29.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.19-1
- Initial package. (using DAR)
