# $Id$
# Authority: dag
# Upstream: Benjamin Trott <ben+cpan@stupidfool.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Blog-Metadata

Summary: Extract common metadata from a weblog
Name: perl-WWW-Blog-Metadata
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Blog-Metadata/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Blog-Metadata-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Class::ErrorHandler)
BuildRequires: perl(Feed::Find)
BuildRequires: perl(HTML::Parser)
BuildRequires: perl(Module::Pluggable::Ordered)
BuildRequires: perl(URI::Fetch)

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
* Tue Aug 19 2008 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
