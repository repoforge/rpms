# $Id$
# Authority: dag
# Upstream: Simon Wistow <simonw$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-Find-Iterator

Summary: Perl module to provide an iterator interface to URI::Find
Name: perl-URI-Find-Iterator
Version: 0.6
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-Find-Iterator/

Source: http://www.cpan.org/modules/by-module/URI/URI-Find-Iterator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-URI-Find-Iterator is a Perl module to provide an iterator interface
to URI::Find.

This package contains the following Perl module:

    URI::Find::Iterator

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
%doc MANIFEST META.yml Readme
%doc %{_mandir}/man3/URI::Find::Iterator.3pm*
%dir %{perl_vendorlib}/URI/
%dir %{perl_vendorlib}/URI/Find/
#%{perl_vendorlib}/URI/Find/Iterator/
%{perl_vendorlib}/URI/Find/Iterator.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.6-1
- Initial package. (using DAR)
