# $Id$
# Authority: dag

### EL6 ships with perl-Unicode-Map8-0.12-20.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-Transliterate

Summary: Perl module named Unicode-Transliterate
Name: perl-Unicode-Transliterate
Version: 0.3
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-Transliterate/

Source: http://www.cpan.org/modules/by-module/Unicode/Unicode-Transliterate.%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Unicode-Transliterate is a Perl module.

This package contains the following Perl module:

    Unicode::Transliterate

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Unicode::Transliterate.3pm*
%dir %{perl_vendorarch}/Unicode/
%{perl_vendorarch}/Unicode/Transliterate.pm
%dir %{perl_vendorarch}/auto/Unicode/
%{perl_vendorarch}/auto/Unicode/Transliterate/

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
