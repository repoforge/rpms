# $Id$
# Authority: dag
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-imap

Summary: Perl module to support IMAP URI
Name: perl-URI-imap
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-imap/

Source: http://www.cpan.org/modules/by-module/URI/URI-imap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-URI-imap is a Perl module to support IMAP URI.

This package contains the following Perl module:

    URI::imap

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
%doc %{_mandir}/man3/URI::imap.3pm*
%dir %{perl_vendorlib}/URI/
#%{perl_vendorlib}/URI/imap/
%{perl_vendorlib}/URI/imap.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
