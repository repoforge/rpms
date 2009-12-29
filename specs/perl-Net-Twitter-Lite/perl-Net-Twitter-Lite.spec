# $Id$
# Authority: shuff
# Upstream: Marc Mims <marc$questright,com>
# ExcludeDist: el3 el4
# Rationale: versions > 0.08000 require perl(URI) >= 1.40, RHEL5 bundles 1.35

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Twitter-Lite

Summary: A perl interface to the Twitter API
Name: perl-%{real_name}
Version: 0.08006
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Twitter-Lite/

Source: http://search.cpan.org/CPAN/authors/id/M/MM/MMIMS/Net-Twitter-Lite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Carp)
BuildRequires: perl(Encode)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(JSON::Any) >= 1.21
BuildRequires: perl(LWP::UserAgent) >= 2.032
BuildRequires: perl(Net::OAuth) >= 0.16
BuildRequires: perl(URI) >= 1.4
BuildRequires: perl(URI::Escape)
BuildRequires: perl >= 5.005
Requires: perl(Carp)
Requires: perl(Encode)
Requires: perl(JSON::Any) >= 1.21
Requires: perl(LWP::UserAgent) >= 2.032
Requires: perl(Net::OAuth) >= 0.16
Requires: perl(URI) >= 1.4
Requires: perl(URI::Escape)
Requires: perl >= 5.005

%filter_from_requires /^perl*/d
%filter_setup

%description
This module provides a perl interface to the Twitter APIs. It uses the same API
definitions as Net::Twitter, but without the extra bells and whistles and
without the additional dependencies. Same great taste, less filling.

This module is related to, but is not part of the Net::Twitter distribution.
It's API methods and API method documentation are generated from Net::Twitter's
internals. It exists for those who cannot, or prefer not to install Moose and
its dependencies.

You should consider upgrading to Net::Twitter for additional functionality,
finer grained control over features, full backwards compatibility with older
versions of Net::Twitter, and additional error handling options.

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
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Net/Twitter
%{perl_vendorlib}/Net/Twitter/Lite.pm
%{perl_vendorlib}/Net/Twitter/Lite

%changelog
* Tue Dec 29 2009 Christoph Maser <cmr@financial.com> - 0.08006-1
- Updated to version 0.08006.
- use --skipdeps since Net::OAuth is not seen

* Wed Dec 09 2009 Steve Huff <shuff@vecna.org> - 0.08005-1
- Initial package.
