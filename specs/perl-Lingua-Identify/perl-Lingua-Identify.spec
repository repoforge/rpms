# $Id$
# Authority: dries
# Upstream: Jos&#233; Alves de Castro <cog$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-Identify

Summary: Identify languages
Name: perl-Lingua-Identify
Version: 0.23
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-Identify/

Source: http://www.cpan.org/modules/by-module/Lingua/Lingua-Identify-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A module which can identify languages.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

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
%doc %{_mandir}/man1/*.1*
%doc %{_mandir}/man3/*.3pm*
%{_bindir}/langident
%{_bindir}/make-lingua-identify-language
%dir %{perl_vendorlib}/Lingua/
%{perl_vendorlib}/Lingua/Identify.pm
%{perl_vendorlib}/Lingua/Identify/

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.23-1
- Updated to version 0.23.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Updated to release 0.19.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Initial package.
