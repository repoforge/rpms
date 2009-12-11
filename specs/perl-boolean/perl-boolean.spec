# $Id$
# Authority: cmr
# Upstream: Ingy döt Net <ingy$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name boolean

Summary: Boolean support for Perl
Name: perl-boolean
Version: 0.20
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/boolean/

Source: http://www.cpan.org/authors/id/I/IN/INGY/boolean-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.005003
Requires: perl >= 5.005003

%description
Boolean support for Perl.

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
%doc %{_mandir}/man3/boolean.3pm*
#%{perl_vendorlib}/boolean/
%{perl_vendorlib}/boolean.pm

%changelog
* Fri Dec 11 2009 Christoph Maser <cmr@financial.com> - 0.20-1
- Initial package. (using DAR)
