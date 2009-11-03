# $Id$
# Authority: dag
# Upstream: SADAHIRO Tomoyuki <SADAHIRO$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-Regex-Set

Summary: Perl module that implements Subtraction and Intersection of Character Sets in Unicode Regular Expressions
Name: perl-Unicode-Regex-Set
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-Regex-Set/

Source: http://www.cpan.org/modules/by-module/Unicode/Unicode-Regex-Set-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Unicode-Regex-Set is a Perl module that implements Subtraction
and Intersection of Character Sets in Unicode Regular Expressions.

This package contains the following Perl module:

    Unicode::Regex::Set

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Unicode::Regex::Set.3pm*
%dir %{perl_vendorlib}/Unicode/
%dir %{perl_vendorlib}/Unicode/Regex/
#%{perl_vendorlib}/Unicode/Regex/Set/
%{perl_vendorlib}/Unicode/Regex/Set.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
