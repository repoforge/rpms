# $Id$
# Authority: shuff
# Upstream: Keith Grennan <kgrennan$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-OAuth

Summary: An implementation of the OAuth protocol
Name: perl-%{real_name}
Version: 0.20
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-OAuth/

Source: http://search.cpan.org/CPAN/authors/id/K/KG/KGRENNAN/Net-OAuth-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Class::Accessor) >= 0.31
BuildRequires: perl(Class::Data::Inheritable) >= 0.06
BuildRequires: perl(Digest::HMAC_SHA1) >= 1.01
BuildRequires: perl(Digest::SHA1) >= 2.12
#BuildRequires: perl(Encode) >= 2.35
BuildRequires: perl(Encode)
BuildRequires: perl(Module::Build::Compat) >= 0.02
#BuildRequires: perl(Test::More) >= 0.66
BuildRequires: perl(Test::More)
BuildRequires: perl(UNIVERSAL::require) >= 0.10
BuildRequires: perl(URI::Escape) >= 3.28
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Class::Accessor) >= 0.31
Requires: perl(Class::Data::Inheritable) >= 0.06
Requires: perl(Digest::HMAC_SHA1) >= 1.01
Requires: perl(Digest::SHA1) >= 2.12
#Requires: perl(Encode) >= 2.35
Requires: perl(Encode)
Requires: perl(Module::Build::Compat) >= 0.02
#Requires: perl(Test::More) >= 0.66
Requires: perl(Test::More)
Requires: perl(UNIVERSAL::require) >= 0.10
Requires: perl(URI::Escape) >= 3.28

# manage perl dependencies manually
%filter_from_requires /^perl.*/d
%filter_setup

%description
OAuth is

"An open protocol to allow secure API authentication in a simple and standard
method from desktop and web applications."

In practical terms, OAuth is a mechanism for a Consumer to request protected
resources from a Service Provider on behalf of a user.

Please refer to the OAuth spec: http://oauth.net/documentation/spec

Net::OAuth provides:

* classes that encapsulate OAuth messages (requests and responses).
* message signing
* message serialization and parsing.
* 2-legged requests (aka. tokenless requests, aka. consumer requests), see
  "CONSUMER REQUESTS"

Net::OAuth does not provide:

* Consumer or Service Provider encapsulation
* token/nonce/key storage/management


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
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Net
%{perl_vendorlib}/Net/OAuth.pm
%{perl_vendorlib}/Net/OAuth/

%changelog
* Wed Dec 09 2009 Steve Huff <shuff@vecna.org> - 0.20-1
- Initial package.
