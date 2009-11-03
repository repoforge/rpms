# $Id$
# Authority: dag
# Upstream: Doug Gorley <dgorley$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SQL-Library
%define real_version v0.0.3

Summary: Perl module for managing simple SQL libraries stored in INI-like files
Name: perl-SQL-Library
Version: 0.0.3
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SQL-Library/

Source: http://www.cpan.org/modules/by-module/SQL/SQL-Library-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-SQL-Library is a Perl module for managing simple SQL libraries
stored in INI-like files.

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
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man3/SQL::Library.3pm*
%dir %{perl_vendorlib}/SQL/
%{perl_vendorlib}/SQL/Library.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.0.3-1
- Initial package. (using DAR)
