# $Id$
# Authority: dag
# Upstream: Benjamin Trott <ben+cpan@stupidfool.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Blog-Metadata

Summary: Extract common metadata from a weblog
Name: perl-WWW-Blog-Metadata
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Blog-Metadata/

Source: http://search.cpan.org/CPAN/authors/id/B/BT/BTROTT/WWW-Blog-Metadata-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Class::ErrorHandler)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Feed::Find)
BuildRequires: perl(HTML::Parser)
BuildRequires: perl(Module::Pluggable::Ordered)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI::Fetch)
BuildRequires: perl >= 5.8.1
Requires: perl(Class::Accessor)
Requires: perl(Class::ErrorHandler)
Requires: perl(Feed::Find)
Requires: perl(HTML::Parser)
Requires: perl(Module::Pluggable::Ordered)
Requires: perl(URI::Fetch)
Requires: perl >= 5.8.1

%filter_from_requires /^perl*/d
%filter_setup

%description
Extract common metadata from a weblog.

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
%doc %{_mandir}/man3/WWW::Blog::Metadata.3pm*
%dir %{perl_vendorlib}/WWW/
%dir %{perl_vendorlib}/WWW/Blog/
#%{perl_vendorlib}/WWW/Blog/Metadata/
%{perl_vendorlib}/WWW/Blog/Metadata.pm

%changelog
* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 0.03-1
- Updated to version 0.03.

* Tue Aug 19 2008 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
