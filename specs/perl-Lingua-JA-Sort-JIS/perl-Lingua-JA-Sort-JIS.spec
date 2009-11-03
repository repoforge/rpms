# $Id$
# Authority: dries
# Upstream: SADAHIRO Tomoyuki <SADAHIRO$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-JA-Sort-JIS

Summary: Compares and sorts strings encoded in UTF-8
Name: perl-Lingua-JA-Sort-JIS
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-JA-Sort-JIS/

Source: http://www.cpan.org/modules/by-module/Lingua/Lingua-JA-Sort-JIS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Compares and sorts strings encoded in UTF-8.

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
%doc Changes README
%doc %{_mandir}/man3/Lingua::JA::Sort::JIS*
%{perl_vendorlib}/Lingua/JA/Sort/JIS.p*
%dir %{perl_vendorlib}/Lingua/JA/Sort/
%dir %{perl_vendorlib}/Lingua/JA/
%dir %{perl_vendorlib}/Lingua/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
